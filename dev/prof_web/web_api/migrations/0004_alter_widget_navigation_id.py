# Generated by Django 5.0.6 on 2024-06-25 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof_api', '0003_alter_content_id_alter_navigation_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='navigation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='widgets', to='prof_api.navigation'),
        ),
    ]
