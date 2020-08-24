#!/usr/bin/env bash
echo "install python and pip3"
apt update
apt install -y python3.7 python3-pip postgresql postgresql-contrib
sudo apt-get install libpq-dev
pip3 install --upgrade pip
pip3 install django==3.1
pip3 install psycopg2

# DB creation
sudo -u postgres createdb givit
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'givit';"
