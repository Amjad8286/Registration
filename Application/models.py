from django.db import models


# Create your models here.

class incidents(models.Model):
    location = models.TextField(max_length=2048)
    incident_department = models.TextField(max_length=2048)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    incident_location = models.TextField(max_length=2048)
    initial_severty = models.TextField(max_length=2048)
    suspected_Cause = models.TextField(max_length=2048)
    immediate_action = models.TextField(max_length=2048)
    Enviromental_Incident = models.CharField(max_length=2048)
    injuryillness = models.CharField(max_length=2048)
    Property_damage = models.CharField(max_length=2048)
    vehicle = models.CharField(max_length=2048)

    def __str__(self):
        return self.incident_location
