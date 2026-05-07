.PHONY: lint dc-build test test.cpython test.pypy test.cpython-latest test.pypy-latest


lint:
	@uvx pre-commit run -a
	@uvx ty check

dc-build:
	@COMPOSE_BAKE=1 docker compose build

test: dc-build test.cpython test.cpython-latest test.pypy test.pypy-latest

test.cpython:
	@docker compose run --rm cpython uv run pytest -vvs

test.cpython-latest:
	@docker compose run --rm cpython-latest uv run pytest -vvs

test.pypy:
	@docker compose run --rm pypy uv run pytest -vvs

test.pypy-latest:
	@docker compose run --rm pypy-latest uv run pytest -vvs