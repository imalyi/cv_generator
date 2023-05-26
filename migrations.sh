#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py makemigrations accounts
python3 manage.py migrate accounts
python3 manage.py makemigrations cv_generator
python3 manage.py migrate cv_generator

export DJANGO_SETTINGS_MODULE=cv_generator.settings
python3 createsuperuser.py
