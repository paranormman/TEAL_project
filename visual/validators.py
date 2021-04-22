from django.core.exceptions import ValidationError
import os
import pandas as pd
# from django.contrib import messages
from requests.api import request
from django.shortcuts import redirect, render


def validate_file(value):

    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.csv']
    if ext.lower() in valid_extentions:
        df=pd.read_csv(value)
        col = df.columns.tolist()
        n = len(col)
        if n == 0:
           raise ValidationError(u'No Column to parse ')
        elif n != 2:
            if col[0] != 'time':
                raise ValidationError('File misses time value, give samplingfrequency value by clicking the button below')
                return redirect("Sampling freq")
            elif col[1] != 'amplitude':
                raise ValidationError('File misses amplitude value')
                # calculate sf and other operations
            raise ValidationError(u'File doesnt have either amplitude or time')
			
            # return render(request, "csvapp/upload.html", data)
        elif n == 2:
            return value
    else:
        raise ValidationError(u'Unsupported file extention. please upload a .csv file. ')







