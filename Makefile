SHELL := /bin/bash
VE_BIN := .env/bin/

setup: setup-virtual-env setup-hooks install-requirements

setup-virtual-env:
	virtualenv --python python3.7 .env

setup-hooks:
	git config core.hooksPath .githooks

install-requirements:
	$(VE_BIN)pip install -r requirements.txt

test-ci:
	pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=src --cov-report=xml --cov-report=html

test:
	$(VE_BIN)python -m pytest tests --cov=src

