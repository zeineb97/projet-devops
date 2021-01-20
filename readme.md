# End of Semester Project

![Project Image](https://dpsvdv74uwwos.cloudfront.net/statics/img/product-pages/devops.png)

> This project is an academic project developed within the framework of validation of the theoretical knowledge and practical skills acquired in the 2 subjects; DevOps and Deployment for students in 5th year software engineering at [INSAT](http://www.insat.rnu.tn) with the option: DevOps and software testing.
---

> Start Project GL5 - Developed by Zeineb Chabchoub

### Table of contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Structure](#structure)
- [Use](#use)
- [Live-Demo](#live-demo)


## Requirements
- Python 3
- Django (3.1)
- Django REST Framework
- Django Rest Auth
- Django Prometheus (2.1)
#### Technologies 
- [Django](https://www.djangoproject.com) :  A Python-based free and open-source web framework 
- [SQlite](https://www.sqlite.org/index.html): SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. 
- [Prometheus](https://prometheus.io) : An open-source monitoring system with a dimensional data model, flexible query language, efficient time series database and modern alerting approach.
- [Grafana](https://grafana.com): Grafana is the open source analytics & monitoring solution for every database.
- [Docker](https://www.docker.com) : Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
- [Docker-compose](https://github.com/docker/compose): Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format.
- [Heroku](heroku.com): Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.   


## Installation
```
	pip install -r requirements.txt
```
## Structure 

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have three resources: 
-  `clients`, so we will use the following URLS - `/clients/` and `/clients/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`clients` | GET | READ | Get all clients
`clients/:id` | GET | READ | Get a single client
`clients`| POST | CREATE | Create a new client
`clients/:id` | PUT | UPDATE | Update a client
`clients/:id` | DELETE | DELETE | Delete a client

- `admin` : an automatic admin interface provided by Django, we use /admin to access to it.
- `Application level metrics endpoint` :  to monitor our application metrics we should navigate to `/metrics`. 



```
Admin credentials : 
- username: admin
- password: 456123
```

## Use

We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
	python manage.py runserver
```

## Live Demo 
This Project is deployed on Heroku. 

- [live-demo-admin-panel](https://devops-project-cd.herokuapp.com/admin)

- [live-demo-clients](https://devops-project-cd.herokuapp.com/clients)

- [live-demo-metrics](https://devops-project-cd.herokuapp.com/metrics )

[Back To The Top ](#End-of-Semester-Project)
