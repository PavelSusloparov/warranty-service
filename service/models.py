from sqlalchemy.orm import relationship

from service import db
from datetime import datetime


class Warranty(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("store.id"), nullable=False)
    store = relationship("Store", backref="warranty")
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    item = relationship("Item", backref="warranty")
    warranty_price = db.Column(db.Float, nullable=False)
    warranty_duration_months = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, store_id, item_id, warranty_price, warranty_duration_months):
        self.store_id = store_id
        self.item_id = item_id
        self.warranty_price = warranty_price
        self.warranty_duration_months = warranty_duration_months

    def __repr__(self):
        return '<Warranty {}. item: {}>'.format(self.id, self.item_id)


class Item(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String, nullable=False)
    sku = db.Column(db.String, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    title = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, _type, sku, cost, title):
        self.type = _type
        self.sku = sku
        self.cost = cost
        self.title = title

    def __repr__(self):
        return '<Item {}. title: {}>'.format(self.id, self.title)


class Store(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    uuid = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, uuid):
        self.uuid = uuid

    def __repr__(self):
        return '<Store {}. uuid: {}>'.format(self.id, self.uuid)
