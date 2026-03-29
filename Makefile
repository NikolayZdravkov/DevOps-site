.PHONY: run test lint install

install:
	venv/bin/pip install -r requirements.txt

run:
	venv/bin/python app.py

test:
	venv/bin/pytest tests/ -v

lint:
	venv/bin/flake8 app.py tests/
