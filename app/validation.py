from rest_framework.exceptions import ValidationError



def validate_int_param(param):
    try:
        param = int(param)
    except (TypeError, ValueError):
        raise ValidationError(detail="Id must be a positive integer")

    if param <= 0:
        raise ValidationError(detail="Id must be a positive integer")