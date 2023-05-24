# Generated by Django 4.2.1 on 2023-05-24 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('tg_username', models.CharField(max_length=255, unique=True)),
                ('tg_chat_id', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.region')),
            ],
        ),
    ]
