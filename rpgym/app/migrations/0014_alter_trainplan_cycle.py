# Generated by Django 4.1 on 2022-08-31 23:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_alter_trainplan_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainplan",
            name="cycle",
            field=models.IntegerField(
                default=None,
                null=True,
                unique=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]