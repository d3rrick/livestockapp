# Livestock decision support system

## Description
The LDSS aids in management of livestock information in Nyeri county, the livestock agency can report various diseases on ivestock, such data is used to predict diseases based on climatic conditions around the year, implements AfricasTalking to warn farmers of incidences reported near them and creation of an api to make data reusable in multiple applications.
Created on, May 19th 2018


## Technologies used
- Django
- Geodjango
- Jquery
- Leafletjs
- HTML5
- Css3
- Postgresql
- Postgis
- Git
- AfricasTalking
- DjangoRestFramework

## Development and Setup.

### prerequisites

Python 2.7 should be installed
django 1.8
install other packages provided in the requirements.txt file
Running the application.
Visit this link to view on any browser.

### Installation.

- Ensure python2.7 is installed.
- Clone the repository git clone
- create a virtual environment virtualenv and activate source /bin/activate
- Install the required packages pip3 install -r requirements.txt
- Create a postgresql database.
- open the psql terminal by typing psql -h localhost -U
- Once on the psql terminal create the database ```CREATE DATABASE ```
- Create postgis extension CREATE EXTENSION postgis and CREATE EXTENSION postgis-topology
- Quit the shell \q
- Once the database is setup, make migrations, this creates database schemas for the application python manage.py -makemigrations
- Then create the actual database tables by python manage.py migrate
- Start the application by python manage.py runserver and open http://127.0.0.1:8000 in the browser.
- Test Driven Development
- Testing was done using python inbuild test tool called unittest to test database and form models.

## Reccomendations
- Implement geo-odk forms for data collection using android phones.
- Disease prediction using machine learning.
- USSD for notifications.

## Further help
To get Further help you can visit the official python and django documentation.

## Licence
MIT (c) 2017 muriithi derrick
