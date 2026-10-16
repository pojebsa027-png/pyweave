PY ?= python3
DJANGO_DIR := django
FLASK_DIR := flask/10-taskapp

.PHONY: help install test test-django test-flask lint clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  %-14s %s\n", $$1, $$2}'

install: ## install both dependency sets
	$(PY) -m pip install -r $(DJANGO_DIR)/requirements.txt
	$(PY) -m pip install -r $(FLASK_DIR)/requirements.txt

test: test-django test-flask ## run every check

test-django: ## Django test suite
	cd $(DJANGO_DIR) && $(PY) manage.py test -v 2

test-flask: ## import-check the finished Flask app
	cd $(FLASK_DIR) && $(PY) -c "import app; print('flask app imports clean')"

lint: ## byte-compile both trees
	$(PY) -m compileall -q $(DJANGO_DIR) $(FLASK_DIR)

clean: ## drop generated artifacts
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -f $(DJANGO_DIR)/db.sqlite3 $(FLASK_DIR)/instance/tasks.db
