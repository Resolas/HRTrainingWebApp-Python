# Generated by Django 4.2.1 on 2023-05-31 11:35

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
                ('role_name', models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee')], max_length=10, null=True)),
                ('email', models.CharField(max_length=45, null=True, unique=True)),
                ('first_name', models.CharField(max_length=45, null=True)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('position', models.CharField(max_length=45, null=True)),
                ('funded_by', models.CharField(max_length=45, null=True)),
                ('annual_salary', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
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
                ('evaluation_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
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
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'evaluation',
            },
        ),
        migrations.CreateModel(
            name='InvestmentReport',
            fields=[
                ('investment_report_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
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
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_reports', to=settings.AUTH_USER_MODEL)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_reports', to='database.evaluation')),
            ],
            options={
                'db_table': 'investment_report',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('training_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=45)),
                ('length_of_service', models.CharField(max_length=45)),
                ('application_date', models.DateField()),
                ('training_name', models.CharField(max_length=45)),
                ('training_provider', models.CharField(max_length=45)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('training_hours', models.IntegerField()),
                ('application_status', models.IntegerField()),
                ('current_status', models.IntegerField()),
                ('delivery_method', models.IntegerField()),
                ('aims_and_objective', models.TextField()),
                ('expected_outcome', models.TextField()),
                ('total_cost', models.IntegerField()),
                ('bjc_contribution', models.TextField()),
                ('employee_contribution', models.TextField()),
                ('employee_qualification', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to=settings.AUTH_USER_MODEL)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='database.evaluation')),
                ('investment_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='database.investmentreport')),
            ],
            options={
                'db_table': 'training',
            },
        ),
        migrations.AddField(
            model_name='investmentreport',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_reports', to='database.training'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='investment_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='database.investmentreport'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='database.training'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='evaluation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_users', to='database.evaluation'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='investment_report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_users', to='database.investmentreport'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_users', to='database.training'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
