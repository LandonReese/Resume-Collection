from django.db import models
from students.models import Student
from instruments.models import Instrument

class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Checkout #{self.id}: {self.student.firstname} {self.student.lastname} - {self.instrument.type}"