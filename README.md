# FastAPI CRUD Demo

## Pre-requisites

- Python 3.12
- Poetry 1.7.1
- Docker

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

Create new team

```bash
curl --location 'http://127.0.0.1:8000/api/team' \
--header 'Content-Type: application/json' \
--data '{
    "name": "New Team",
    "description": "Description of New Team"
}'
```

List all teams

```bash
curl --location 'http://127.0.0.1:8000/api/team/'
```

Get team by id

```bash
curl --location 'http://127.0.0.1:8000/api/team/9921ef59-16e8-43ce-be7d-d9d9a1ebe8fc'
```

Update team

```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/team/ecfa80a2-fa56-4503-a812-985d8a0069f9' \
--header 'Content-Type: application/json' \
--data '{
    "description": "Description of New Team Updated"
}'
```

Delete team

```
curl --location --request DELETE 'http://127.0.0.1:8000/api/team/ecfa80a2-fa56-4503-a812-985d8a0069f9'
```