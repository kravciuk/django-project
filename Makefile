SHELL := /bin/bash
CURRENT_DIR = $(shell pwd)

all: ;@echo 'Run with option (install, run, syncdb, etc...)'

up: pull migrate static reload
fup: pull reload

var:
	mkdir -p var var/htdocs/static var/spooler var/htdocs/media var/htdocs/protected var/logs var/backup;

config:
	cp etc/nginx.example.conf etc/nginx.conf;
	cp etc/supervisor.example.conf etc/supervisor.conf;
	cp etc/uwsgi.example.ini etc/uwsgi.ini;

pull:
	git pull;

run:
	poetry run python src/manage.py runserver 127.0.0.1:8000;

http:
	poetry ./.venv/bin/activate && uwsgi --ini etc/uwsgi.ini:http

uwsgi:
	source ./.venv/bin/activate && uwsgi --ini etc/uwsgi.ini:uwsgi_daemon

reload:
	source ./.venv/bin/activate && uwsgi --reload var/uwsgi.pid

kill:
	kill -9 `cat var/uwsgi.pid`

celery:
	source ./.venv/bin/activate && celery --workdir=src -A project worker -l debug -C

flower:
	source ./.venv/bin/activate && celery flower -A project --workdir=src --address=127.0.0.1 --port=5555

static:
	poetry run python src/manage.py collectstatic --noinput

console:
	poetry run python src/manage.py ${app} --traceback

migrate:
	poetry run python src/manage.py migrate

fakemigrate:
	poetry run python src/manage.py migrate --fake ${app}

commit:
	poetry run python src/manage.py makemigrations  ${app}

locale:
	poetry run python src/manage.py makemessages -a -s --ignore=env/* --ignore=var/* --keep-pot  -v3 --no-location

compilemessages:
	poetry run python src/manage.py compilemessages

help:
	poetry run python src/manage.py help

# password managment
passwd:
	poetry run python src/manage.py changepassword

adduser:
	poetry run python src/manage.py createsuperuser

shell:
	poetry run python src/manage.py shell

install:
	poetry install --keep-outdated ${app}
