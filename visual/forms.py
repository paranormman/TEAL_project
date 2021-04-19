from django import forms
from .models import SourceFile, SampleField
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
                df=pd.read_csv(upload)
                n = len(df.columns.tolist())
                if n == 0:
                    raise forms.ValidationError(u'No Column to parse ')
                elif n == 1:
                    # take sf as input from user and other operations
                    raise forms.ValidationError(u'No time value in the file ')
                elif n == 2:
                    # calculate sf and other operations
                    raise forms.ValidationError(u'Missing amplitude value in the file')
                else:
                    return upload

        else:
            raise forms.ValidationError("Please upload a .csv extention files only")
        
        return upload

def clean(self):
    cleaned_data = super(UploadFileForm, self, clean)
    upload = cleaned_data.get('file')
    return upload



class SampleForm(forms.ModelForm):

    class Meta:
        model = SampleField
        fields = ('sampling_frequency',)