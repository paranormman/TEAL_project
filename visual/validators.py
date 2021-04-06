from django.core.exceptions import ValidationError
import os


def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.csv']
    if not ext.lower() in valid_extentions:
        raise ValidationError(u'Unsupported file extention. please upload a .csv file. ')
    else:
        return value





    # value= str(value)
    # if value.endswith(".csv") != True: 
    #     raise ValidationError("Only PDF and Word Documents can be uploaded")
    # else:
    #     return value