.PHONY: help test dev build release

.DEFAULT: help
help:
	@echo "make help"
	@echo "    echo help information."
	@echo "make test"
	@echo "    run test cases."
	@echo "make dev"
	@echo "    init develop environment."

dev:
	python3 -m venv venv

venv:
	source venv/bin/activate

build: venv
	python -m pip install --upgrade build
	python -m build

release: venv
	python -m pip install --upgrade twine
	python -m twine upload dist/*
