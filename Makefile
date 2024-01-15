.PHONY: up down logs status start-local check-code-quality fix-code-quality test test-coverage help
.DEFAULT_GOAL := help
app-name = fastapi_crud_demo
run-docker-compose = docker compose -f docker-compose.yml
run-uvicorn = uvicorn
run-pytest = poetry run pytest
run-black = poetry run black
run-isort = poetry run isort
run-flake8 = poetry run flake8
run-bandit = poetry run bandit

up: # Start containers and tail logs
	$(run-docker-compose) up -d

down: # Stop all containers
	$(run-docker-compose) down --remove-orphans

logs: # Tail container logs
	$(run-docker-compose) logs -f postgres

status: # Show status of all containers
	$(run-docker-compose) ps

start-local: # Start dev environment
	$(run-uvicorn) $(app-name).main:app --reload

test:
ifdef filter
	$(run-pytest) $(filter) -vv
else
	$(run-pytest) -vv
endif

test-coverage: test
	$(run-pytest) --cov-report term-missing --cov=$(app-name)

check-code-quality: # Run code quality checks
	$(run-black) --check $(app-name)
	$(run-isort) --check-only $(app-name)
	$(run-flake8) $(app-name)
	$(run-bandit) -r $(app-name)

fix-code-quality: # Fix code quality issues
	$(run-black) $(app-name)
	$(run-isort) $(app-name)
	$(run-flake8) $(app-name)
	$(run-bandit) -r $(app-name)

help: # make help
	@awk 'BEGIN {FS = ":.*#"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?#/ { printf "  \033[36m%-27s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
