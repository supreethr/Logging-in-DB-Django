# Logging-in-DB-Django
Errors are Handled by Middleware and Logging in DB Django

###Middleware
ExceptionMiddleware: Gets the exception and converts into 200 and sends the json of error message

###Database Routing
LogRouter: Database routes log database and normal database

###Database Logging Handler
DBHandler: Handler helps in saving Log information in specific model

## Getting Started

### Prerequisites

What things you need to install the software and how to install them

```
Django==1.11.17
djangorestframework==3.9.0
pkg-resources==0.0.0
pytz==2018.7
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
$ virtualenv venv
$ source venv/bin/activate
```

And install requirements

```
$ pip install -r requirements.txt
```

##Running Server
```
$python manage.py createsuperuser
$Username: upwards
$password: qwe@12345
```

##Working API
```
http://localhost:8000/api/exception_views
```

##CRUD Operation in Django Admin
Login with above credentials

## Built With

* [Python](https://www.python.org/) - The tool used
* [Django](https://www.django-rest-framework.org/) - Django Rest Framework

## Authors

* **Supreeth Ravi** - *supreethsln@gmail.com* - [LinkedIn](https://linkedin.com/in/supreeth-ravi-0313078b/)
