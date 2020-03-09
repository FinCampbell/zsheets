from django.db import models

# Create your models here.

class Schedule(models.Model):
    def __str__(self):
        return "Schedule Object"

    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thusday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()

class Employee(models.Model):
    #employeeID = models.AutoField(primary_key=True) #Django creates it's
    # own primary keys called id. This can be used if desired.

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    salary = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete = models.CASCADE)

    def __str__(self):
        return self.firstName

    def returnSchedule(self):
        return schedule

#class Manager(models.Model):
