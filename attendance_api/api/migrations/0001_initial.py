# Generated by Django 2.2 on 2019-05-18 14:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fileds', models.CharField(default='', max_length=500)),
                ('qualification', models.CharField(default='', max_length=201)),
                ('contact_no', models.CharField(default='', max_length=25)),
                ('gender', models.IntegerField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='UploadStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='upload_location')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=1)),
                ('gender', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('section', models.CharField(max_length=201)),
                ('slug', models.SlugField(default='1', max_length=251)),
                ('roll_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='Semester_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
                ('section', models.CharField(max_length=201)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
            ],
        ),
        migrations.CreateModel(
            name='add_student_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('subject', models.CharField(max_length=201)),
                ('batch', models.CharField(max_length=201)),
                ('date', models.CharField(max_length=201)),
                ('attend', models.IntegerField(default=0)),
                ('professer_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Facultys')),
                ('student_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Students')),
            ],
        ),
    ]
