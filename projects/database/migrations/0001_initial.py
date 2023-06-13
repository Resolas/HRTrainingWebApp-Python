# Generated by Django 4.2.1 on 2023-06-13 11:14

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('employee_id', models.IntegerField(unique=True, verbose_name=models.AutoField(primary_key=True, verbose_name=''))),
                ('role_name', models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee')], max_length=10, null=True)),
                ('email', models.CharField(max_length=45, null=True, unique=True)),
                ('first_name', models.CharField(max_length=45, null=True)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('position', models.CharField(max_length=45, null=True)),
                ('funded_by', models.CharField(max_length=45, null=True)),
                ('gross_salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('daily_salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('half_salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'custom_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=45)),
                ('job_title', models.CharField(max_length=45)),
                ('training_course', models.TextField()),
                ('training_provider', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('certification', models.IntegerField()),
                ('certification_reason', models.TextField()),
                ('objective', models.TextField()),
                ('topics', models.TextField()),
                ('usefulness', models.TextField()),
                ('three_important_points', models.TextField()),
                ('topic_relevant', models.IntegerField()),
                ('encouragement', models.IntegerField()),
                ('material_helpfulness', models.IntegerField()),
                ('objective_met', models.IntegerField()),
                ('time_sufficient', models.IntegerField()),
                ('expectation_met', models.IntegerField()),
            ],
            options={
                'db_table': 'evaluation',
            },
        ),
        migrations.CreateModel(
            name='InvestmentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=45)),
                ('scale', models.CharField(max_length=45)),
                ('point_on_scale', models.DecimalField(decimal_places=0, max_digits=10)),
                ('funded_by', models.CharField(max_length=45)),
                ('annual_salary', models.DecimalField(decimal_places=0, max_digits=10)),
                ('weekly_hours', models.DecimalField(decimal_places=0, max_digits=10)),
                ('gross_weekly', models.DecimalField(decimal_places=0, max_digits=10)),
                ('full_day_rate', models.DecimalField(decimal_places=0, max_digits=10)),
                ('half_day_rate', models.DecimalField(decimal_places=0, max_digits=10)),
                ('hourly_rate', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'investment_report',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=45)),
                ('employee_position', models.CharField(max_length=45)),
                ('length_of_service', models.CharField(max_length=45)),
                ('application_date', models.DateField()),
                ('programme_name', models.CharField(max_length=45)),
                ('training_provider', models.CharField(max_length=45)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('no_of_hours', models.IntegerField()),
                ('delivery_method', models.IntegerField()),
                ('programme_aims', models.TextField()),
                ('programme_objectives', models.TextField()),
                ('expected_outcome', models.TextField()),
                ('bjc_contribution', models.TextField()),
                ('emp_contribution', models.IntegerField()),
                ('training_hours', models.IntegerField(null=True)),
                ('application_status', models.IntegerField(null=True)),
                ('current_status', models.IntegerField(null=True)),
                ('total_cost', models.IntegerField(null=True)),
                ('employee_contribution', models.TextField()),
                ('employee_qualification', models.TextField()),
                ('employee_signed', models.TextField()),
                ('administrator_signed', models.TextField()),
            ],
            options={
                'db_table': 'training',
            },
        ),
        migrations.CreateModel(
            name='UserTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.training')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_training',
            },
        ),
        migrations.CreateModel(
            name='UserInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.investmentreport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_investment',
            },
        ),
        migrations.CreateModel(
            name='UserEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.evaluation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_evaluation',
            },
        ),
    ]
