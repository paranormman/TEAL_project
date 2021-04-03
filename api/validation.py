from django.core.exceptions import ValidationError
import pandas as pd



def validate_file(value):
    value= str(value)
    if value.endswith(".csv") != True: 
        raise ValidationError("Only CSV can be uploaded")

    decoded_file = value.read().decode('ISO-8859-1').splitlines()
    reader = value.DictReader(decoded_file)
    headers = []
    # for row in csv.DictReader(csv_file, delimiter=',', quotechar='|'):
    for row in reader:
        headers = [x.lower() for x in list(row.keys())]
        break

    if 'amplitude' not in headers or 'time' not in headers:
        raise ValidationError(
            'CSV file must have "time" column and "amplitude column')
    else:
        return value