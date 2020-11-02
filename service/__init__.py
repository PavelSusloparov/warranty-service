import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from dotenv import load_dotenv
from pathlib import Path

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
application.config['AWS_ACCESS_KEY'] = os.environ.get('AWS_ACCESS_KEY')
application.config['AWS_SECRET_KEY'] = os.environ.get('AWS_SECRET_KEY')
application.config['S3_BUCKET_NAME'] = os.environ.get('S3_BUCKET_NAME')
db = SQLAlchemy(application)
migrate = Migrate(application, db)
ma = Marshmallow(application)

from service import routes, models
