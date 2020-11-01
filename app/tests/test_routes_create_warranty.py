from app.tests.test_helpers import create_warranty
from app.tests.test_base import client


def test_create_warranty_happy_path(client):
    store_uuid = "b21ad0676f26439"
    item_type = "furniture"
    item_sku = "986kjeo8fy9qhu"
    item_cost = 150.0
    item_title = "Amy's Sectional Sofa"

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost,
        item_title=item_title
    )
    assert response.status_code == 202
    assert response.json['item']['type'] == item_type
    assert response.json['item']['sku'] == item_sku
    assert response.json['item']['cost'] == item_cost
    assert response.json['item']['title'] == item_title
    assert response.json['item']['created_at'] is not None
    assert response.json['item']['updated_at'] is None

    assert response.json['store']['uuid'] == store_uuid
    assert response.json['store']['created_at'] is not None
    assert response.json['store']['updated_at'] is None

    assert response.json['warranty_price'] is not None
    assert response.json['warranty_price'] is not None
    assert response.json['warranty_duration_months'] is not None
    assert response.json['created_at'] is not None
    assert response.json['updated_at'] is None


def test_create_warranty_many_none_store_uuid(client):
    item_sku = "986kjeo8fy9qhu"
    item_cost = 150.0
    item_title = "Amy's Sectional Sofa"

    response = create_warranty(
        client=client,
        store_uuid=None,
        item_type=None,
        item_sku=item_sku,
        item_cost=item_cost,
        item_title=item_title
    )
    assert 400 == response.status_code
    assert response.json['errors']['item_type'][0] == "Field may not be null."
    assert response.json['errors']['store_uuid'][0] == "Field may not be null."


def test_create_warranty_many_empty_store_uuid(client):
    item_sku = "986kjeo8fy9qhu"
    item_cost = 150.0
    item_title = "Amy's Sectional Sofa"

    response = client.post(
        '/warranties',
        json=dict(
            item_sku=item_sku,
            item_cost=item_cost,
            item_title=item_title
        ),
        follow_redirects=True
    )
    assert response.status_code == 400
    assert response.json['errors']['item_type'][0] == "Missing data for required field."
    assert response.json['errors']['store_uuid'][0] == "Missing data for required field."


def test_create_warranty_wrong_item_cost_format(client):
    store_uuid = "b21ad0676f26439"
    item_type = "furniture"
    item_sku = "986kjeo8fy9qhu"
    item_cost = "item_cost"
    item_title = "Amy's Sectional Sofa"

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost,
        item_title=item_title
    )
    assert response.status_code == 400
    assert response.json['errors']['item_cost'][0] == "Not a valid number."

