MODULE := HackCurl

run:
	@python HackCurl/app.py

test-all: lint test
	@echo "--"

test:
	@pytest

format:
	@black

lint: type-check
	@echo "\n--BLACK--\n"
	@black .
	@echo "\n--FLAKE8--\n"
	@flake8

type-check:
	@mypy .

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml .mypy_cache

.PHONY: clean test
