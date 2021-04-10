from django.core.exceptions import ValidationError
import os
import pandas as pd


def validate_file(value):

    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.csv']
    if ext.lower() in valid_extentions:
        csv = pd.read_csv(value.name)
        if csv.isnull().any()['time']:
            raise ValidationError(u'Missing time value data')
        elif csv.isnull().any()['amplitude']:
            raise ValidationError(u'Missing Amplitude value data')
        # csv = pd.read_csv(value, header=0, nrows=0).columns.tolist()
        # first = csv.index('time')
        # second = csv.index('amplitude')
        # if first != 0:
        #     raise ValidationError(u'Missing time value data')
        # elif second != 1:
        #     raise ValidationError(u'Missing Amplitude value data')
        else:
            return value
    else:
        raise ValidationError(u'Unsupported file extention. please upload a .csv file. ')





