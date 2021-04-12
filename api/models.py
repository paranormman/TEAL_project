from django.db import models
from . validation import validate_file

class Files(models.Model):
    file = models.FileField(validators=[validate_file], blank = False, null = False)
    remark = models.CharField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add=True)


# creating sampling frequency IntegerField

class SamplingFrequency(models.Model):
    samplingFrequency = models.IntegerField(max_length= 50)

