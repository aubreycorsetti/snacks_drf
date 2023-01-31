# Lab 28

## Author: Aubrey Corsetti

### How to run tests:
python manage.py runserver
Navigate to snacks/tests
Run in terminal: python manage.py test

#### Setup
python3.11 -m venv .venv
pip install django
pip install djangorestframe
django-admin startproject snacks_api_project .
python manage.py startapp snacks
python manage.py createsuperuser
python manage.py makemigrations snacks
python manage.py migrate
python manage.py runserver


Load the site at http://0.0.0.0:8001/api/v1/snacks/