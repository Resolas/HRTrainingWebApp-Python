# HRTrainingWebApp-Python
HR web app run with python django instead of Java due to complications with the java project

Migrate to new database for sqlite3

Delete migration files before that:
database/migrations


1. python makemigrations database
2. python migrate
3. python manage.py createsuperuser (Do the following steps, new username, email, password)
4. python manage.py runserver

Done
