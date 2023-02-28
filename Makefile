install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=sites_count --cov-report xml

lint:
	poetry run flake8 sites_count

isort:
	poetry run isort sites_count

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

ipython:
	poetry run ipython

.PHONY: install test lint isort selfcheck check build ipython