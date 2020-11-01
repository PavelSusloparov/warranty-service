import os
import threading
from datetime import datetime
import json
import random

import boto3

from app import flask_app, db
from flask import request, jsonify

from app.models import Warranty, Store, Item
from app.schema import warranty_schema, warranty_schema_list, create_warranty_schema, get_warranty_schema

TEMP_FILE_NAME = 'temp.txt'


@flask_app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


@flask_app.route('/warranties', methods=['POST'])
def create_warranty():
    data = request.get_json()
    errors = create_warranty_schema.validate(data=data)
    if errors:
        return jsonify(dict(errors=errors)), 400

    store = store_fetch_or_create(data)
    item = item_fetch_or_create(data)
    warranty = warranty_create(store.id, item.id)
    response = warranty_schema.jsonify(warranty)

    thread = threading.Thread(target=upload_s3, args=(response.json,))
    thread.start()

    return response, 202


@flask_app.route('/warranties', methods=['GET'])
def get_warranties():
    args = request.args
    if args.get("sku") is None and args.get("item_type") is None and args.get("store_uuid") is None:
        warranties = Warranty.query.all()
        return jsonify(warranty_schema_list.dump(warranties))

    errors = get_warranty_schema.validate(data=args)
    if errors:
        return jsonify(dict(errors=errors)), 400

    item = Item.query.filter_by(type=args['item_type'], sku=args['sku']).first()
    if item is None:
        errors['item'] = ["item does not exist for given item_type and sku"]
    store = Store.query.filter_by(uuid=args['store_uuid']).first()
    if store is None:
        errors['store'] = ["store does not exist for given store_uuid"]
    if errors:
        return jsonify(dict(errors=errors)), 400

    warranties = Warranty.query.filter_by(item_id=item.id, store_id=store.id).all()
    return jsonify(warranty_schema_list.dump(warranties))


def upload_s3(warranty_json):
    with open(TEMP_FILE_NAME, 'w') as f:
        json.dump(warranty_json, f, sort_keys=True, indent=4)
    s3 = boto3.client('s3',
                      aws_access_key_id='AKIAIHBUYDKNIT3ZBYSQ',
                      aws_secret_access_key='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',
                      )
    with open(TEMP_FILE_NAME, "rb") as f:
        s3.upload_fileobj(f, "warranty-service", "warranty-%s.txt" % warranty_json['id'])
    os.remove(TEMP_FILE_NAME)


def store_fetch_or_create(data):
    store = Store.query.filter_by(uuid=data['store_uuid']).first()
    if store is None:
        store = Store(uuid=data['store_uuid'])
        db.session.add(store)
        db.session.commit()
    return store


def item_fetch_or_create(data):
    item = Item.query.filter_by(
        type=data['item_type'],
        sku=data['item_sku'],
        cost=data['item_cost'],
        title=data['item_title']).first()
    if item is None:
        item = Item(
            _type=data['item_type'],
            sku=data['item_sku'],
            cost=data['item_cost'],
            title=data['item_title']
        )
        db.session.add(item)
        db.session.commit()
    return item


def warranty_create(store_id, item_id):
    warranty = Warranty(
        store_id=store_id,
        item_id=item_id,
        warranty_price=random.randint(100, 20000) / random.randint(1, 10),
        warranty_duration_months=random.randint(1, 12)
    )
    db.session.add(warranty)
    db.session.commit()
    return warranty
