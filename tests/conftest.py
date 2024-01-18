import pytest
from starlette.testclient import TestClient

from main import app
from models.team import TeamCreate


@pytest.fixture(scope="function")
def client():
    # app.dependency_overrides[get_session] = lambda: session
    with TestClient(app) as c:
        yield c


@pytest.fixture
def team_id():
    return "eab7624c-bcd0-4d4c-95e3-bac60e8ba98d"


@pytest.fixture
def new_team_request():
    def _new_team_request(name: str = None, description: str = None):
        return TeamCreate(
            name=name or "Team 1",
            description=description or "Team 1 description",
        )

    return _new_team_request

