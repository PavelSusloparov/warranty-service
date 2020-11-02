# Curl commands

## Local

### POST /warranties
```
curl -X POST -H "Content-Type: application/json" -d '{"store_uuid": "b21ad0676f26439", "item_type": "furniture", "item_sku": "986kjeo8fy9qhu", "item_cost": 150.0, "item_title": "Amy Sectional Sofa"}' http://127.0.0.1:5000/warranties
```

### GET /warranties
```
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/warranties?sku=986kjeo8fy9qhu&item_type=furniture&store_uuid=b21ad0676f26439
```

## Remote

### POST /warranties
```
curl -k -X POST -H "Content-Type: application/json" -d '{"store_uuid": "b21ad0676f26439", "item_type": "furniture", "item_sku": "986kjeo8fy9qhu", "item_cost": 150.0, "item_title": "Amy Sectional Sofa"}' https://develop.eba-vppbjmsc.us-east-1.elasticbeanstalk.com/warranties
```

### GET /warranties
```
curl -k -X GET -H "Content-Type: application/json" https://develop.eba-vppbjmsc.us-east-1.elasticbeanstalk.com/warranties?sku=986kjeo8fy9qhu&item_type=furniture&store_uuid=b21ad0676f26439
```

