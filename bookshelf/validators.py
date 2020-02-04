import os
from django.core.validators import ValidationError


def validate_extension_csv(value):
    extension = os.path.splitext(value.name)[1]
    valid_ext = ['.csv']
    if not extension.lower() in valid_ext:
        raise ValidationError('File not valid!')