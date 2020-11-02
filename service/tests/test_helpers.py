

def create_warranty(client, store_uuid, item_type, item_sku, item_cost, item_title):
    return client.post(
        '/warranties',
        json=dict(
            store_uuid=store_uuid,
            item_type=item_type,
            item_sku=item_sku,
            item_cost=item_cost,
            item_title=item_title
        ),
        follow_redirects=True
    )


def get_warranty(client, sku, item_type, store_uuid):
    query_params = "?"
    if sku is not None:
        query_params += "sku=%s&" % sku
    if item_type is not None:
        query_params += "item_type=%s&" % item_type
    if store_uuid is not None:
        query_params += "store_uuid=%s&" % store_uuid
    return client.get(
        '/warranties%s' % query_params,
        follow_redirects=True
    )
