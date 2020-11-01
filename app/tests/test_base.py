from app import flask_app
import pytest
import os
import tempfile
from app import db


@pytest.fixture
def client():
    db_fd, flask_app.config['DATABASE'] = tempfile.mkstemp()
    flask_app.config['WTF_CSRF_ENABLED'] = False
    flask_app.config['DEBUG'] = False
    flask_app.config['TESTING'] = True

    with flask_app.test_client() as client:
        with flask_app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(flask_app.config['DATABASE'])


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Hello World!' in rv.data
