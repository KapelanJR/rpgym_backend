# Generated by Django 4.0.6 on 2022-07-15 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_trainhistory_plan_module'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='muslce_part',
            new_name='muscle_part',
        ),
    ]