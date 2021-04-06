from django.db import models
from . validators import validate_file

# Create your models here.
class SourceFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="media/", validators=[validate_file])

    def __str__(self):
        return self.name + ": " + str(self.filepath)