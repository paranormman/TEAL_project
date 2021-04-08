from django import forms
from .models import SourceFile
from .validators import validate_file
from . import views
from rest_framework import settings
import pandas as pd

class UploadFileForm(forms.ModelForm):


    class Meta:
        model = SourceFile
        fields = ('file',)


    def clean_csv_file(self):
        upload = self.cleaned_data['file']

        if upload:
            filename = upload.name
            if filename.endswith(settings.FILE_UPLOAD_TYPE):
                csv = pd.read_csv(upload, header=0, nrows=0).columns.tolist()
                first = csv.index('time')
                second = csv.index('amplitude')
                
                if first != 0:
                    raise forms.ValidationError(
                        "File dosen't have time value")

                elif second != 1:
                    raise forms.ValidationError(
                        "There is no amplitude value")
                
                else:
                    return upload

        else:
            raise forms.ValidationError("Please upload a .csv extention files only")
        
        return upload

def clean(self):
    cleaned_data = super(UploadFileForm, self, clean)
    upload = cleaned_data.get('file')
    return upload