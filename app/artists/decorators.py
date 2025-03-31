import code
from functools import wraps
from django.http import JsonResponse

from app.artists.exceptions import APIException


def handle_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except APIException as e:
            return JsonResponse(
                {'error': e.detail, 'code': e.code},
                status=e.code
            )
        except Exception as e:
            return JsonResponse(
                {'error': 'Internal Server Error', code: 500},
                status=500
            )
    return wrapper