# Generated by Django 3.1.7 on 2021-04-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='incidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=2048)),
                ('incident_department', models.TextField(max_length=2048)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('incident_location', models.TextField(max_length=2048)),
                ('initial_severty', models.TextField(max_length=2048)),
                ('suspected_Cause', models.TextField(max_length=2048)),
                ('immediate_action', models.TextField(max_length=2048)),
                ('Enviromental_Incident', models.CharField(max_length=2048)),
                ('injuryillness', models.CharField(max_length=2048)),
                ('Property_damage', models.CharField(max_length=2048)),
                ('vehicle', models.CharField(max_length=2048)),
            ],
        ),
    ]
