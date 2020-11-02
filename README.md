# Overview

System where thousands of retail stores are concurrently sending product data to a service that generates warranties based on item cost and type.
Each warranty is tied to a store.

The service provides API that will allow creation and retrieval of warranties.

## Service

The service is flask/python 3.7/sqlite application.

### /warranties (POST request):
- POST requests sent to the service will have a payload in the following format: 
```
    {
        "store_uuid": "b21ad0676f26439",
        "item_type": "furniture",
        "item_sku": "986kjeo8fy9qhu,
        "item_cost": 150.0,
        "item_title": "Amy's Sectional Sofa"
    }
```
		
a) Request is validated.

b) The data is saved in three tables: Store, Item, Warranty. If Store or Item do not exist, new records are created.
    Warranty has a relationship to store and item objects.
    
c) After creating the warranty object, a new thread that uploads the current payload and response to a S3 bucket on AWS.
    The thread does not block the API response from being sent.
    
d) API response includes the warranty object that was just created.

### /warranties (GET request)

- GET requests to this endpoint returns warranties for a given sku, item_type, or store_uuid.
An example GET request URL would be the following: /warranties?sku=sku-12345&item_type=furniture&store_uuid=b21ad0676f26439.

a) If any of query parameters exist, all query parameters are validated. all sku, item_type, store_uuid are present.
    If none of query parameters exist, all existent warranties are returned.

Code is covered with unit and integration tests.
Unit tests test modules of code.
Integration tests test endpoints, listed above.

The service is deployed to AWS using Elastic Beanstalk - [Link](http://develop.eba-vppbjmsc.us-east-1.elasticbeanstalk.com/).

The service uploads newly created warranties as a non-blocking thread to public [S3 bucket](https://s3.console.aws.amazon.com/s3/buckets/warranty-service?region=us-east-1)


# Assumptions

1. The service is a basic services and uses SQLite database, which does not allow concurrent requests. Use MySql or Postqres to support simultaneous calls use case.

2. The tech description does not provide any modeling requirements for item. I used separate Item model to store item related data. Warranty has a foreign key to item.

3. It is not clear from the tech description on item type and sku combination uniqueness.
Assumption was made and unique constraint setup on this fields during commit.
Meaning two items can not be inserted if they have same type and sku.
```
GET /warranties
/warranties?sku=986kjeo8fy9qhu&item_type=furniture&store_uuid=b21ad0676f26439
```

## Local development

Create venv
```
python3 -m venv ./venv
```

Activate venv
```
. venv/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt
```

Create a `.env` file with secrets in the project root. Provide your values
```
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
S3_BUCKET_NAME=
```

Run tests
```
pytest
```

Run application
```
FLASK_ENV=development FLASK_APP=service flask run
```
