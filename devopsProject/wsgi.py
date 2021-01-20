"""
WSGI config for devopsProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

"""
The Web Server Gateway Interface:a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. 
It describes how a web server communicates with web applications, and how web applications can be chained together to process one request. 
It is used to forward requests from a web server (such as Apache or NGINX) to a backend Python web application or framework. 
From there, responses are then passed back to the web server to reply to the requestor.
Requests are sent from the client’s browser to the server. 

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devopsProject.settings')

application = get_wsgi_application()
