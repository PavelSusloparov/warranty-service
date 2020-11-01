import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['AWS_ACCESS_KEY'] = os.environ.get('AWS_ACCESS_KEY')
flask_app.config['AWS_SECRET_KEY'] = os.environ.get('AWS_SECRET_KEY')
flask_app.config['S3_BUCKET_NAME'] = os.environ.get('S3_BUCKET_NAME')
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)
ma = Marshmallow(flask_app)

from app import routes, models
