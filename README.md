# FastAPI CRUD Demo

## Pre-requisites

- Python 3.12
- Poetry 1.7.1
- Docker

## Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
poetry install
```

## Environment variables

Duplicate the `.env.dist` file and rename it to `.env`. Then, fill in the values for the environment variables.

## Commands

Start docker containers:
```bash
make up
```

Stop docker containers:
```bash
make down
```

Start local server
```bash
make start-local
```

Create new migration
```bash
make create-migration name=<migration_name>
```

Apply migrations
```bash
make migrate
```

Launch tests
```bash
make test
```

Launch test with coverage
```bash
make coverage
```

Check code quality
```bash
make check-code-quality
```

Fix code quality
```bash
make fix-code-quality
```

## Use cases

Register user

```bash
curl --location 'http://<server_url>/api/user/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": <email>,
    "password": <password>
}'
```

Login user

```bash
curl --location 'http://<server_url>/api/user/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": <email>,
    "password": <password>
}'
```

It will return a token that you can use to access the protected endpoints.
```
{"access_token":"<access_token>","token_type":"bearer"}
```

Get current user

```bash
curl --location 'http://<server_url>/api/user/me' \
--header 'Authorization: Bearer <access_token>'
```

Create new team

```bash
curl --location 'http://<server_url>/api/team' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token> \
--data '{
    "name": "New Team",
    "description": "Description of New Team"
}'
```

List all teams

```bash
curl --location 'http://<server_url>/api/team/' \
--header 'Authorization: Bearer <access_token> \
```

Get team by id

```bash
curl --location 'http://<server_url>/api/team/9921ef59-16e8-43ce-be7d-d9d9a1ebe8fc' \
--header 'Authorization: Bearer <access_token> \
```

Update team

```bash
curl --location --request PATCH 'http://<server_url>/api/team/ecfa80a2-fa56-4503-a812-985d8a0069f9' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token> \
--data '{
    "description": "Description of New Team Updated"
}'
```

Delete team

```bash
curl --location --request DELETE 'http://<server_url>/api/team/ecfa80a2-fa56-4503-a812-985d8a0069f9' \
--header 'Authorization: Bearer <access_token> \
```

## OpenAPI

You can access the OpenAPI documentation at http://<server_url>/docs