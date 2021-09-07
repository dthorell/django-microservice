# Django Microservice Template
A Django project template for microservices.

## How to install

Install virtualenv dependencies using:

```
$ pipenv install django djangorestframework whitenoise
```

Create folder structure:
```
$ mkdir src
```

Create a new project based on this template using:

```
$ pipenv shell
$ django-admin.py startproject --template=https://github.com/dthorell/django-microservice/archive/master.zip project_name src
```
