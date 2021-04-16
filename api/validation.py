from django.core.exceptions import ValidationError
import pandas as pd
import logging




def validate_file(value):
    path = 'E:\\Django_proj\\restapi\\media\\Acc_time_ext.csv'
    value= str(value)
    if value.endswith(".csv") == True:
        try:
            df = pd.read_csv(path)
            n = len(df.columns.tolist())
            if n == 0:
                raise ValidationError(u'No Column to parse ')
            elif n == 1:
                raise ValidationError(u'No time value in the file ')
            elif n == 2:
                raise ValidationError(u'Missing amplitude value in the file')
            else:
                return value
        except Exception as e:
            logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
            raise ValidationError("Unable to upload CVS file. "+repr(e))
        
    else:
        raise ValidationError("Unappropriate File type, Only .CSV can be uploaded")

    # df=pd.read_csv(value)
    # if not ("time" in df.columns.tolist() and "amplitude" in df.columns.tolist()):
    #     raise ValidationError('CSV file must have "time" column and "amplitude column')
    # else:
    #     return value