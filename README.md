# ToDo Web Application:
My First Web App on Django

This is my first web app on Django. This app creates todo lists and todo activity to each todo list. Application also has a feature of deling Todos</br>


# Description:
This project consists of 3 main parts: </br>
  1 - Top page - illustrates the list of Todo lists</br>
  2 - Detail page - illustrates the list of todos of the chosen Todo list</br>
  3 - Search page - searches all matching Todos and Todo lists.</br>

Application also has a function of deleting Todos and Todo lists. Moreover, Todos can be marked as done or undone. 

# Instalation:

1 * Install Python https://www.python.org/downloads/ (Do not forget to register variable on Windows) </br>
2 * Install Django with the following come $ pip install -e django/ (Windows cmd | Linux, Mac = terminal)</br>
3 * Then Install the following 3rd party application - django-bootstrap3-datetimepicker (https://github.com/nkunihiko/django-bootstrap3-datetimepicker) - <code>pip install django-bootstrap3-datetimepicker</code> The following addon was abandoned 2 years ago and is not compactible with django 1.11.1. Therefore, with the help of the community, I made some changes to widgets.py </br>
4 * Install crispy forms - http://django-crispy-forms.readthedocs.io/en/latest/install.html</br>

5 * Open terminal or command promt and enter following </br>
<code>python manage.py makemigrations</code></br>
<code>python manage.py migrate</code></br>
<code>python manage.py runserver</code></br>
And web application will be available on localhost 127.0.0.1

# Requirements:
This project was done under following environment
Python = 3.6</br>
Django >= 1.11.1</br>
Crispy Forms</br>
Bootstrap 3</br>

# Live Demo
http://disctanger.webfactional.com/
