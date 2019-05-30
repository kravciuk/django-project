SHELL := /bin/bash
CURRENT_DIR = $(shell pwd)

all: ;@echo 'Run with option (install, run, syncdb, etc...)'

install: var requirements migrate
up: pull migrate static reload

var:
	mkdir -p var var/htdocs/static var/spooler var/htdocs/media var/htdocs/protected var/logs var/backup;

config:
	cp etc/nginx.example.conf etc/nginx.conf;
	cp etc/supervisor.example.conf etc/supervisor.conf;
	cp etc/uwsgi.example.ini etc/uwsgi.ini;

requirements:
	pipenv sync;

pull:
	git pull;

run:
	pipenv run python src/manage.py runserver 127.0.0.1:8000;

urun:
	source ./env/bin/activate && uwsgi --ini etc/uwsgi.ini:dev

uwsgi:
	source ./env/bin/activate && uwsgi --ini etc/uwsgi.ini:uwsgi_daemon

reload:
	source ./env/bin/activate && uwsgi --reload var/uwsgi.pid

kill:
	kill -9 `cat var/uwsgi.pid`

celery:
	source ./env/bin/activate && celery --workdir=src -A project worker -l debug -C

flower:
	source ./env/bin/activate && celery flower -A project --workdir=src --address=127.0.0.1 --port=5555

static:
	pipenv run python src/manage.py collectstatic --noinput

console:
	pipenv run python src/manage.py ${app} --traceback

migrate:
	pipenv run python src/manage.py migrate

fakemigrate:
	pipenv run python src/manage.py migrate --fake ${app}

commit:
	pipenv run python src/manage.py makemigrations  ${app}

locale:
	pipenv run python src/manage.py makemessages -a -s --ignore=env/* --ignore=var/* --keep-pot  -v3 --no-location

compilemessages:
	pipenv run python src/manage.py compilemessages

help:
	pipenv run python src/manage.py help

# password managment
passwd:
	pipenv run python src/manage.py changepassword

adduser:
	pipenv run python src/manage.py createsuperuser

shell:
	pipenv run python src/manage.py shell
