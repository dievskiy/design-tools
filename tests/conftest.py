import pytest
from app import create_app
from config import Config


@pytest.fixture
def app():
    test_config = Config()
    test_config.TESTING = True

    tools = create_app(test_config)
    yield tools


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
