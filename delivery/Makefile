clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']

test:
	FLASK_ENV=test pytest tests/ -v --cov=delivery

init_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db init
	FLASK_APP=delivery/app.py flask db migrate
	FLASK_APP=delivery/app.py flask db upgrade