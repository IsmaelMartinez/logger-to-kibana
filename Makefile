SHELL := /bin/bash
VE_BIN := .env/bin/
AWS_DEFAULT_REGION=eu-west-1
AWS_REGION=$(AWS_DEFAULT_REGION)

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

lint:
	python -m flake8 src test

run:
	python main.py process_generate_and_send -f /projects/BIP/payments/legacy-subscription-service
