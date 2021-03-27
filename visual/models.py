from django.db import models

# Create your models here.
class FFT(models.Model):
    time = models.FloatField()
    amplitude = models.FloatField()
    # frequency = models.FloatField()
