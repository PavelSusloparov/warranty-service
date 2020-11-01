from marshmallow_sqlalchemy import fields

from app import ma
from app.models import Warranty, Store
from marshmallow import fields, Schema


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Warranty
        load_instance = True
        include_relationships = True
        fields = ('id', 'type', 'sku', 'cost', 'title', 'created_at', 'updated_at')


item_schema = ItemSchema()
item_schema_list = ItemSchema(many=True)


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store
        load_instance = True
        include_relationships = True
        fields = ('id', 'uuid', 'created_at', 'updated_at')


store_schema = StoreSchema(many=True)
store_schema_list = StoreSchema()


class WarrantySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Warranty
        load_instance = True
        include_relationships = True
        fields = ('id', 'store', 'item', 'warranty_price', 'warranty_duration_months', 'created_at', 'updated_at')

    store = fields.Nested(StoreSchema)
    item = fields.Nested(ItemSchema)


warranty_schema = WarrantySchema()
warranty_schema_list = WarrantySchema(many=True)


class CreateWarrantySchema(Schema):

    item_type = fields.Str(required=True)
    item_sku = fields.Str(required=True)
    item_cost = fields.Float(required=True)
    item_title = fields.Str(required=True)
    store_uuid = fields.Str(required=True)


create_warranty_schema = CreateWarrantySchema()


class GetWarrantySchema(Schema):

    sku = fields.Str(required=True)
    item_type = fields.Str(required=True)
    store_uuid = fields.Str(required=True)


get_warranty_schema = GetWarrantySchema()
