backend capstone project.
littel lemon project.
structions for run project :
pipenv shell
pipenv install django
django-admin startproject littlelemon .
python manage.py startapp restaurant
Open the settings.py file from the littlelemon project package in a new VS Code window. Add the restaurant app to the INSTALLED_APPS list.
python manage.py runserver
this paroject is developed by python version 3.11 
if your python version is different fromthis change python version in pipfile

for test run : 
python manage.py test tests/

list of apis:
http://127.0.0.1:8000/api/booking/tables/
http://127.0.0.1:8000/api/menu/
http://127.0.0.1:8000/api/
http://127.0.0.1:8000/api/api-token-auth/

users : 
username : adminpassword:Lemon@123
thoken : 0401e1c7ac9f6bc7d600f23b863c0a369c31f473