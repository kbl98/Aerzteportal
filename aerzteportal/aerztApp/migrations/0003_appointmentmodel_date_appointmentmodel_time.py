# Generated by Django 4.2.3 on 2023-07-30 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerztApp', '0002_alter_appointmentmodel_doctor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
