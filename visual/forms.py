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
                csv = pd.read_csv(upload.name)
                

                if csv.isnull().any()['time']:
                    raise forms.ValidationError(u'Missing time value data')

                elif csv.isnull().any()['amplitude']:
                    raise forms.ValidationError(u'Missing amplitude value data')
                
                else:
                    return upload

        else:
            raise forms.ValidationError("Please upload a .csv extention files only")
        
        return upload

def clean(self):
    cleaned_data = super(UploadFileForm, self, clean)
    upload = cleaned_data.get('file')
    return upload