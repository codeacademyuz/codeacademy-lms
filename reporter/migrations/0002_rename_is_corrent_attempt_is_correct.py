# Generated by Django 4.2.1 on 2023-05-29 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attempt',
            old_name='is_corrent',
            new_name='is_correct',
        ),
    ]
