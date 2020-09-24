#!/usr/bin/env bash

# Installing packages
sudo apt update
sudo apt install -y python3.7 python3.7-dev python3-pip postgresql postgresql-contrib libpq-dev postgresql-common postgresql-client #postgresql-devel
sudo pip3 install --upgrade pip

# Installing pipenv, create new env and sync lib with pipfile
sudo pip3 install pipenv

#navigate to app folder
if [ "$CI" ] 
then
    cd givitsite
    echo "in github action CI"
    
else
    cd /vagrant/givitsite/
    echo "in vagrant"
fi

pipenv sync

# start posgresql when running out of vagrant
if [ "$CI" ] 
then
    echo "start postgresql"
    sudo systemctl start postgresql
fi

# DB creation
sudo -u postgres createdb givit
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'givit';"

# run the server in background
pipenv run python3 manage.py migrate
nohup pipenv run python3 manage.py runserver 0:8000 &
nohup pipenv run python3 manage.py process_tasks &
