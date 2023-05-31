# Generated by Django 4.2.1 on 2023-05-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_test_table_testtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('evaluation_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=45)),
                ('job_title', models.CharField(max_length=45)),
                ('training_course', models.BinaryField()),
                ('training_provider', models.BinaryField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('certification', models.BooleanField()),
                ('certification_reason', models.TextField()),
                ('objective', models.TextField()),
                ('topics', models.TextField()),
                ('usefulness', models.TextField()),
                ('three_important_points', models.TextField()),
                ('topic_relevant', models.CharField(max_length=45)),
                ('encouragement', models.CharField(max_length=45)),
                ('material_helpfulness', models.CharField(max_length=45)),
                ('objective_met', models.CharField(max_length=45)),
                ('time_sufficient', models.CharField(max_length=45)),
                ('expectation_met', models.CharField(max_length=45)),
                ('admin_id', models.CharField(max_length=20)),
                ('investment_report_id', models.CharField(max_length=20)),
                ('employee_id', models.CharField(max_length=20)),
                ('training_id', models.CharField(max_length=20)),
            ],
        ),
    ]