# Generated by Django 5.0.6 on 2024-06-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationhistory',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='widgethistory',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
