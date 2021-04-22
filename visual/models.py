from django.db import models
from . validators import validate_file

# Create your models here.
class SourceFile(models.Model):
    file = models.FileField(upload_to="media/", validators=[validate_file])
    title = models.CharField(max_length=255)    

    def __str__(self):
        return self.name + ": " + str(self.filepath)

class SampleField(models.Model):
    timefile = models.FileField(upload_to="media/")
    sampling_frequency = models.IntegerField(default=0, null=False)
