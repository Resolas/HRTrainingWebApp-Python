# Generated by Django 4.2.1 on 2023-06-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_evaluation_training_application_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]