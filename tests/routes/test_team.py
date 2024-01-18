from http import HTTPStatus


def test_list_all(client):
    response = client.get("/api/team")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == []


def test_get(client, team_id):
    response = client.get(f"/api/team/{team_id}")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": team_id,
        "name": "Team 1",
        "description": "Team 1 description",
    }


def test_create(client, new_team_request):
    payload = new_team_request()
    response = client.post(
        "/api/team",
        content=payload.model_dump_json(),
    )

    assert response.status_code == HTTPStatus.CREATED
    response_model = response.json()
    assert response_model["id"] is not None
    assert len(response_model["id"]) == 36
    assert response_model["name"] == "Team 1"
    assert response_model["description"] == "Team 1 description"


def test_update(client, team_id, new_team_request):
    payload = new_team_request(
        name="Team 1 Updated",
        description="Team 1 Description Updated",
    )
    response = client.patch(
        f"/api/team/{team_id}",
        content=payload.model_dump_json(),
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": team_id,
        "name": "Team 1 Updated",
        "description": "Team 1 Description Updated",
    }


def test_delete(client, team_id):
    response = client.delete(f"/api/team/{team_id}")

    assert response.status_code == HTTPStatus.NO_CONTENT
