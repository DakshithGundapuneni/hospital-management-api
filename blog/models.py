from django.db import models

# Create your models here.
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    op_fee = models.DecimalField(max_digits=8, decimal_places=2)
    available_days = models.CharField(max_length=100)   # e.g. "Mon, Wed, Fri"
    available_time = models.CharField(max_length=50)    # e.g. "10:00 AM - 2:00 PM"
    contact = models.CharField(max_length=50, blank=True)  # optional phone/email

    def __str__(self):
        return f"{self.name} ({self.specialization})"

