from django.core.exceptions import ValidationError
import os
import pandas as pd


def validate_file(value):

    name = os.path.splitext(value)
    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.csv']
    if ext.lower() in valid_extentions:
        try:
            df=pd.read_csv(name)
            n = len(df.columns.tolist())
            if n == 0:
                raise ValidationError(u'No Column to parse ')
            elif n == 1:
                # take sf as input from user and other operations
                raise ValidationError(u'No time value in the file ')
            elif n == 2:
                # calculate sf and other operations
                raise ValidationError(u'Missing amplitude value in the file')
            else:
                raise ValidationError(u'XXXXXX ')
   
        except:
            raise ValidationError(u'Unsupported file extention. please upload a .csv file. ')

#old exception class 
    # ext = os.path.splitext(value.name)[1]
    # valid_extentions = ['.csv']
    # if ext.lower() in valid_extentions:
    #     csv = os.path(value)
    #     csv = pd.read_csv(ext, header=0, nrows=0).columns.tolist()
    #     first = csv.index('time')
    #     second = csv.index('amplitude')
    #     if first != 0:
    #         raise ValidationError(u'Missing time value data')
    #     elif second != 1:
    #         raise ValidationError(u'Missing Amplitude value data')
    #     else:
    #         return value
    # else:
    #     raise ValidationError(u'Unsupported file extention. please upload a .csv file. ')

# import os
# import pandas as pd
# # path='.\data\CDC_trend_1.csv'
# path='Empty.csv'
# name, extension = os.path.splitext(path)
# if extension =='.csv':
#    try:
#        df=pd.read_csv(path)
#        n=len(df.columns.tolist())
#        if n==0:
#            print('No columns to parse')
#        elif n==1:
#            # take sf as input from user and other operations
#            print('1 coulmn')
#        elif n==2:
#            # calculate sf and other operations
#            print('2 columns')
#        else:
#            print('invalid file format')
   
#    except:
#        print('Bla Bla')





