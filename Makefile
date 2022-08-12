MODULE := HackCurl

run:
	@python HackCurl/app.py

test:
	@pytest

format:
	@black

lint:
	@echo "\n--BLACK--\n"
	@black .
	@echo "\n--FLAKE8--\n"
	@flake8

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml

.PHONY: clean test
