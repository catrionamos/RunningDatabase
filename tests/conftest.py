#import necessary packages for testing purposes
import pytest
#Allow for mock connection to postgresql database
from unittest.mock import MagicMock
from run import app as flask_app

#use decorator to make function reuseable as a test fixture that will set up data and resources.
@pytest.fixture
#create a test app, disabling CSRF for testing purpose.
def app():
    flask_app.config.update({"TESTING":True, "WTF_CSRF_ENABLED":False,"SECRET_KEY":"test_secret_key"})
    #yield will pause the fixture to pass the app instance to the test function
    yield flask_app

@pytest.fixture
#create a simulated web browser to test the HTTP requests.
def client(app):
    return app.test_client()

@pytest.fixture
#create a mock database so the tests do not need the real running_db database.
def mock_db(monkeypatch):
    #Replace db_connect with a fake PostgreSQL connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    monkeypatch.setattr("app.routes.db_connect",lambda:mock_conn)
    return mock_cursor
