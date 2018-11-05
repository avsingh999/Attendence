# Generated by Django 2.1.3 on 2018-11-05 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20181105_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.AlterField(
            model_name='semester_1',
            name='professerr_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.pro'),
        ),
    ]
