# Generated by Django 2.1.3 on 2018-11-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_students_sem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_no', models.IntegerField()),
                ('subject_name', models.CharField(max_length=201)),
                ('subject_code', models.CharField(max_length=201)),
            ],
        ),
    ]
