# Generated by Django 4.1.6 on 2023-02-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30, null=True)),
                ('event_type', models.CharField(max_length=30, null=True)),
                ('desc', models.TextField()),
            ],
        ),
    ]
