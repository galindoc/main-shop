path = src
files = `find $(path) -name '*.py'`

run:
	pipenv run python manage.py runserver

migrations:
	pipenv run python manage.py makemigrations

migrate:
	pipenv run python manage.py migrate

superuser:
	pipenv run python manage.py createsuperuser
