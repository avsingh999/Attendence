# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-05 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20181105_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester_2',
            name='professerr_name',
        ),
        migrations.RemoveField(
            model_name='semester_3',
            name='professerr_name',
        ),
        migrations.RemoveField(
            model_name='semester_4',
            name='professerr_name',
        ),
        migrations.RemoveField(
            model_name='semester_5',
            name='professerr_name',
        ),
        migrations.RemoveField(
            model_name='semester_6',
            name='professerr_name',
        ),
        migrations.RemoveField(
            model_name='semester_7',
            name='professerr_name',
        ),
        migrations.RemoveField(
            model_name='semester_8',
            name='professerr_name',
        ),
        migrations.AddField(
            model_name='semester_2',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AddField(
            model_name='semester_3',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AddField(
            model_name='semester_4',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AddField(
            model_name='semester_5',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AddField(
            model_name='semester_6',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AddField(
            model_name='semester_7',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AddField(
            model_name='semester_8',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
        migrations.AlterField(
            model_name='semester_1',
            name='professer_name',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
    ]
