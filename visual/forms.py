from django import forms
from .models import SourceFile
from .validators import validate_file

class UploadFileForm(forms.ModelForm):
    file = forms.FileField(label = 'CSV File upload:', required = 'True', validators = [validate_file])

    class Meta:
        model = SourceFile
        fields = ('file', 'title')