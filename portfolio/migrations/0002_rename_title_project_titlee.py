# Generated by Django 4.0.5 on 2022-07-03 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='titlee',
        ),
    ]
