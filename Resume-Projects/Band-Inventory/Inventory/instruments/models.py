from django.db import models

# Create your models here.

class Instrument(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    type = models.CharField(max_length=50, blank=False)
    serial_num = models.CharField(max_length=50, blank=True)
    maker = models.CharField(max_length=50, blank=False)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.id} | {self.maker} {self.type}"