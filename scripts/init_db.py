from application import db
from application.models import Warranty, Store, Item
from application.schema import WarrantySchema, StoreSchema, ItemSchema

db.create_all()
warranty_schema = WarrantySchema()
store_schema = StoreSchema()
item_schema = ItemSchema()

store = Store(
    uuid="b21ad0676f26439"
)
db.session.add(store)

item = Item(
    _type="furniture",
    sku="986kjeo8fy9qhu",
    cost=150.0,
    title="Amy's Sectional Sofa"
)
db.session.add(item)
db.session.commit()

warranty_first = Warranty(
    store_id=store.id,
    item_id=item.id,
    warranty_price=10.7,
    warranty_duration_months=4
)
db.session.add(warranty_first)

item = Item(
    _type="light",
    sku="186azkjeo8fy9qba",
    cost=75.5,
    title="Bed light"
)
db.session.add(item)
db.session.commit()

warranty_second = Warranty(
    store_id=store.id,
    item_id=item.id,
    warranty_price=5.2,
    warranty_duration_months=8
)
db.session.add(warranty_second)
db.session.commit()
