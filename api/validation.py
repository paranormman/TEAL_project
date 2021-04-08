from django.core.exceptions import ValidationError
import pandas as pd



def validate_file(value):
    value= str(value)
    if value.endswith(".csv") != True: 
        raise ValidationError("Only CSV can be uploaded")
    # df=pd.read_csv(value)
    # if not ("time" in df.columns.tolist() and "amplitude" in df.columns.tolist()):
    #     raise ValidationError('CSV file must have "time" column and "amplitude column')
    else:
        return value