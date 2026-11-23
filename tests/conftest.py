import pytest
from unittest.mock import MagicMock
from run import app as flask_app

#test app with CSRF turned off so the forms can be posted in tests
@pytest.fixture
def app():
    flask_app.config.update({"TESTING":True, "WTF_CSRF_ENABLED":False,"SECRET_KEY":"test_secret_key"})
    yield flask_app

#simulated web browser to send requests to the app
@pytest.fixture
def client(app):
    return app.test_client()

#replace db_connect with a fake connection so the tests do not need the real database
@pytest.fixture
def mock_db(monkeypatch):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    monkeypatch.setattr("app.routes.db_connect",lambda:mock_conn)
    return mock_cursor
