# Generated by Django 2.1.3 on 2018-11-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20181104_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultys',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
