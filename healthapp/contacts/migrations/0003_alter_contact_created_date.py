# Generated by Django 3.2.2 on 2021-09-05 08:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 5, 8, 3, 49, 399504, tzinfo=utc)),
        ),
    ]
