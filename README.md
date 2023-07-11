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



**User Manual/Guides**


[Start a new Django project cheat sheet.docx](https://github.com/Resolas/HRTrainingWebApp-Python/files/12013876/Start.a.new.Django.project.cheat.sheet.docx)



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

    Text Editor Used:
    Visual Studio Code

    Version:
    Python Version - Python 3.11.1

    Pip Version - pip 23.1.2

    Install:
    Bootstrap - pip install crispy-bootstrap4

**What Works/Doesn't**
    
    What works:
    Login System
    Register Employee
    Create New Application
    Evaluation Form
    Change User Password (Rudimentary)

    What doesn't work/exist:
    Reports
    Evaluation Pie/Bar Charts
    No Autocomplete in Forms
    Correct Details Required in Applications and Evaluations

<img width="576" alt="Admin Screen Functions" src="https://github.com/Resolas/HRTrainingWebApp-Python/assets/64108044/d2798c71-6bee-4728-925d-af09945b91db">

<img width="576" alt="Employee Screen Functions" src="https://github.com/Resolas/HRTrainingWebApp-Python/assets/64108044/fe0ca96b-0021-46d4-b9b9-0656137cbdb7">



    
