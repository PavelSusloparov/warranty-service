from app.tests.test_helpers import create_warranty, get_warranty
from app.tests.test_base import client


def test_get_warranty_happy_path(client):
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

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost + 10.0,
        item_title="%s%s" % (item_title, "_updated"),
    )
    assert response.status_code == 202

    # we have one store and two items and two warranties at this point
    response = get_warranty(
        client=client,
        sku=item_sku,
        item_type=item_type,
        store_uuid=store_uuid
    )
    assert response.status_code == 200
    assert len(response.json) >= 2


def test_get_warranty_fetch_all(client):
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

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost + 10.0,
        item_title="%s%s" % (item_title, "_updated"),
    )
    assert response.status_code == 202

    # we have one store and two items and two warranties at this point
    response = get_warranty(
        client=client,
        sku=None,
        item_type=None,
        store_uuid=None
    )
    assert response.status_code == 200
    assert len(response.json) >= 2


def test_get_warranty_only_one_query_param_provided(client):
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

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost + 10.0,
        item_title="%s%s" % (item_title, "_updated"),
    )
    assert response.status_code == 202

    response = get_warranty(
        client=client,
        sku=None,
        item_type=None,
        store_uuid=store_uuid
    )
    assert response.status_code == 400
    assert response.json['errors']['sku'][0] == "Missing data for required field."
    assert response.json['errors']['item_type'][0] == "Missing data for required field."


def test_get_warranty_happy_path(client):
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

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost + 10.0,
        item_title="%s%s" % (item_title, "_updated"),
    )
    assert response.status_code == 202

    # we have one store and two items and two warranties at this point
    response = get_warranty(
        client=client,
        sku="%s%s" % (item_sku, "_updated"),
        item_type=item_type,
        store_uuid=store_uuid
    )
    assert response.status_code == 400
    assert response.json['errors']['item'][0] == "item does not exist for given item_type and sku"


def test_get_warranty_happy_path(client):
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

    response = create_warranty(
        client=client,
        store_uuid=store_uuid,
        item_type=item_type,
        item_sku=item_sku,
        item_cost=item_cost + 10.0,
        item_title="%s%s" % (item_title, "_updated"),
    )
    assert response.status_code == 202

    # we have one store and two items and two warranties at this point
    response = get_warranty(
        client=client,
        sku=item_sku,
        item_type=item_type,
        store_uuid="%s%s" % (store_uuid, "_updated"),
    )
    assert response.status_code == 400
    assert response.json['errors']['store'][0] == "store does not exist for given store_uuid"
