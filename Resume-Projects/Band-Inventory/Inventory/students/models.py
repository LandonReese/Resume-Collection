from django.db import models

# Create your models here.
# Blank=False means that the field is required
# blank=True 
class Student(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip = models.IntegerField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.id} | {self.firstname} {self.lastname}"