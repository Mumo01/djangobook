# Generated by Django 5.1.6 on 2025-02-21 21:27

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpost',
            name='publication_date',
            field=models.DateField(validators=[api.validators.validate_publication_date]),
        ),
    ]
