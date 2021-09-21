# Generated by Django 3.2.2 on 2021-09-05 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancer',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='covid',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='heart_disease',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='kidney',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='liver',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
