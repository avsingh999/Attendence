# Generated by Django 2.1.3 on 2018-11-05 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20181105_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultys',
            name='section',
        ),
        migrations.RemoveField(
            model_name='students',
            name='section',
        ),
        migrations.AlterField(
            model_name='semester_1',
            name='professerr_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Facultys'),
        ),
    ]
