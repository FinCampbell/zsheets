from django.db import models

from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_employee_profile(sender, instance, created, **kwargs):
        if created:
            Employee.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_employee_profile(sender, instance, **kwargs):
        instance.employee.save()

class Manager(models.Model):
    employee_account = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='manager_account')

    def approve_timesheet(self, timesheet):
        timesheet.approved_status = True

    def __str__(self):
        return self.employee_account.user.username


class Timesheet(models.Model):
    week_beginning = models.DateField()

    monday = models.IntegerField(default=0)
    tuesday = models.IntegerField(default=0)
    wednesday = models.IntegerField(default=0)
    thursday = models.IntegerField(default=0)
    friday = models.IntegerField(default=0)

    approved_status = models.BooleanField(default=False)

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        permissions = [
                ("can_approve", "Can approve timesheets"),
                ("can_search", "Can search employees' timesheets"),
        ]


    def __str__(self):
        return str(self.week_beginning)





