#!/usr/bin/env bash

# Installing packages
apt update
apt install -y python3.7 python3.7-dev python3-pip postgresql postgresql-contrib libpq-dev postgresql-common postgresql-client #postgresql-devel
pip3 install --upgrade pip

# Installing pipenv, create new env and sync lib with pipfile
pip3 install pipenv
cd /vagrant/givitsite/
pipenv sync

# DB creation
sudo -u postgres createdb givit
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'givit';"

# run the server in background
pipenv run python3 manage.py migrate
nohup pipenv run python3 manage.py runserver 0:8000 &
