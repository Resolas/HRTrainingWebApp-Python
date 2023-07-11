# HRTrainingWebApp-Python
HR web app run with python django instead of Java due to complications with the java project



**Web Application Overview**
This is an internal use web application for use by **Human Resources** administrator and their employees to upskill and apply for a training course, to streamline workflow for the HR admin to by automating certain processes.

How the web application supposed to work is to allow employees to apply for training by filling out a form which then will be captured sent into the database, then the admin can then approve/deny the application to give the employee the go ahead or not. If denied the admin can give a reason for the denied application. Once approved the employee can do their respective course. When the application has hit its end date, an evaluation form will appear for that application and is only visible to the attending employee until submitted which is then visible for the admin to read/review.

This project is not yet completed and will be handed over to other teams for further development and deployment of the web application.


**Team members/Contributors**
- Munfung - https://github.com/Resolas
- Chris - https://github.com/Chris-Slattery
- Liam - https://github.com/theprogrammer0
- Marc - https://github.com/m4csam1l1an
- Fazilat - https://github.com/ifshs
- Alwin - https://github.com/alwinjohny



**User Manual**





**Configuration Notes**


    Migrations
    
    Migrate to new database for sqlite3
    
    Delete migration files before that:
    database/migrations
    
    
    1. python makemigrations database
    2. python migrate
    3. python manage.py createsuperuser (Do the following steps, new username, email, password)
    4. python manage.py runserver
    
    Done

**Setup Notes**

    Setup

    Python Version - Python 3.11.1
    

