SHELL := /bin/bash
CURRENT_DIR = $(shell pwd)

all: ;@echo 'Run with option (install, run, syncdb, etc...)'

install: var requirements syncdb
up: pull migrate static

var:
	mkdir -p var var/htdocs/static var/spooler var/htdocs/media var/htdocs/protected var/logs;

config:
	cp etc/nginx.example.conf etc/nginx.conf;
	cp etc/supervisor.example.conf etc/supervisor.conf;
	cp etc/uwsgi.example.ini etc/uwsgi.ini;

requirements:
	source ./env/bin/activate && pip install -r requirements.txt;

run:
	source ./env/bin/activate && python src/manage.py runserver 127.0.0.1:8000;

pull:
	git pull;

uwsgi:
	source ./env/bin/activate && uwsgi --ini etc/uwsgi.ini:uwsgi_daemon

celery:
	source ./env/bin/activate && celery --workdir=src -A project worker -l debug

celery-help:
	source ./env/bin/activate && python src/manage.py celeryd --help

reload:
	source ./env/bin/activate && uwsgi --reload var/uwsgi.pid

kill:
	kill -9 `cat var/uwsgi.pid`

syncdb:
	source ./env/bin/activate && python src/manage.py syncdb;

static:
	source ./env/bin/activate && python src/manage.py collectstatic --noinput

console:
	source ./env/bin/activate && python src/manage.py ${app} --traceback

migrate:
	source ./env/bin/activate && python src/manage.py migrate

fakemigrate:
	source ./env/bin/activate && python src/manage.py migrate --fake ${app}

commit:
	source ./env/bin/activate && python src/manage.py makemigrations  ${app}

locale:
	source ./env/bin/activate && python src/manage.py makemessages -a -s --ignore=env/* --ignore=var/* --keep-pot  -v3 --no-location

compilemessages:
	source ./env/bin/activate && python src/manage.py compilemessages

help:
	source ./env/bin/activate && python src/manage.py help

# password managment
passwd:
	source ./env/bin/activate && python src/manage.py changepassword

adduser:
	source ./env/bin/activate && python src/manage.py createsuperuser

shell:
	source ./env/bin/activate && python src/manage.py shell
