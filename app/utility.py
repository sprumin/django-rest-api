from django.http import JsonResponse

from app.models import Apikey


def authorization(original_function):
    def wrapper_function(*args, **kwargs):
        if not Apikey.objects.filter(api_key=args[0].META.get("HTTP_AUTHORIZATION", None)).exists():
            return JsonResponse({
                "message": "Invalid api-key"
            }, status=400)
        return original_function(*args, **kwargs)
    return wrapper_function
