# Employeemanagment

## 1.Install python

install python 3.8 or greater

## 2.Create virtual environment

## 3.Install packages from requirement.txt

pip install -r requirements.txt

## 4.Setup a local database
To run the application locally, you need to setup a postgres database on your system.
Install postgres (Linux) sudo apt install postgresql libpq-dev
Login as the 'postgres' user and start postgres shell
sudo su - postgres
psql

Install Postgres(Windows)
https://www.postgresql.org/

Create a user for use with the application.
Remember to wrap your password in single quotes.

create user empuser with password 'empuseruserpassword';

Create a database and give permissions for the above user

create database employemangemnt;

grant ALL privileges on database employemangemnt to empuser;

Give permissions to the user to create database so that test databses can be created

ALTER USER empuser CREATEDB;
The url for database is you have created is as following.
DATABASE_URL=postgres://empuser:empuseruserpassword@localhost:5432/employemangemnt
Later, update the DATABASE_URL in .env file.
## 5. Setup .env files
Use example env files create local .env files
cp env.example .env
note: Uses the respective db URLs in .env file.
## 6.Run migration
once everything setup run migration by
python manage.py makemigrations
python manage.py migrate
## 7.Run Server
once migration is successfull run server by
python manage.py runserver

Thank You
