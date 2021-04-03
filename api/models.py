from django.db import models
from . validation import validate_file

class Files(models.Model):
    file = models.FileField(verbose_name='Files', validators=[validate_file], blank = False, null = False)
    remark = models.CharField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
class Atributes(models.Model):
    time = models.FloatField()
    amplitude = models.FloatField()
    sampling_frequency = models.FloatField(verbose_name="Sampling Frequency") 


