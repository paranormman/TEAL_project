from django.core.exceptions import ValidationError
import os
import pandas as pd


def validate_file(value):

    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.csv']
    if ext.lower() in valid_extentions:
        df=pd.read_csv(value)
        n = len(df.columns.tolist())
        if n == 0:
            raise ValidationError(u'No Column to parse ')
        elif n == 1:
                # take sf as input from user and other operations
            raise ValidationError(u'missing time value in the file ')
        elif n == 2:
                # calculate sf and other operations
            raise ValidationError(u'Missing amplitude value in the file')
        else:
            return value
    else:
        raise ValidationError(u'Unsupported file extention. please upload a .csv file. ')







