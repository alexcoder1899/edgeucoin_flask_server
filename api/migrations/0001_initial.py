# Generated by Django 4.2.4 on 2023-08-10 08:10

import api.models
from django.conf import settings
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
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('image', models.FileField(blank=True, null=True, upload_to=api.models.upload_to)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('school', 'School'), ('student', 'Student'), ('teacher', 'Teacher'), ('parent', 'Parent')], default='teacher', max_length=8)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('score', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('incomplete', 'Incomplete'), ('completed', 'Completed')], default='incomplete', max_length=20)),
                ('view_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('Elementary School', 'Elementary'), ('Middle School', 'Middle'), ('High School', 'High')], default='Elementary School', max_length=20)),
                ('contact', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('contact_2', models.CharField(blank=True, max_length=80, null=True)),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('extras', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6)),
                ('athlete', models.BooleanField(default=False)),
                ('college_bound', models.BooleanField(default=False)),
                ('workforce_bound', models.BooleanField(default=False)),
                ('coin', models.IntegerField(default=0)),
                ('interests', models.JSONField(null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.JSONField(null=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.school')),
                ('students', models.ManyToManyField(blank=True, to='api.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('coin', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.upload_to)),
                ('schools', models.ManyToManyField(blank=True, to='api.school')),
                ('students', models.ManyToManyField(blank=True, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('note', models.CharField(blank=True, max_length=1000)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.goal')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.school')),
                ('students', models.ManyToManyField(blank=True, to='api.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('responses', models.JSONField(null=True)),
                ('type', models.CharField(choices=[('Academic', 'Academic'), ('Behavioral', 'Behavioral'), ('Parent', 'Parent')], default='Behavioral', max_length=20)),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='goal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.goals'),
        ),
        migrations.AddField(
            model_name='goal',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='goal',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.student'),
        ),
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.IntegerField(default=0)),
                ('explain', models.CharField(blank=True, max_length=255)),
                ('goal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.goal')),
            ],
        ),
    ]
