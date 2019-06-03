from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .utility import authorization

import json

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


@method_decorator(authorization, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request, user_id=None):
        if user_id:
            try:
                user = User.objects.get(idx=user_id)
            except:
                return JsonResponse({
                    "message": f"user_id '{user_id}' is invalid user"
                }, status=404)

            user_data = {
                "idx": user.idx,
                "email": user.email,
                "username": user.username,
                "info": user.info
            }
        else:
            user = User.objects.all()
            user_data = list()

            for row in user:
                user_data.append({
                    "idx": row.idx,
                    "email": row.email,
                    "username": row.username,
                    "info": row.info
                })

        return JsonResponse({
            "message": user_data
        }, status=200)

    def post(self, request, user_id=None):
        if user_id:
            return JsonResponse({
                "message": "POST method not support parameter"
            }, status=400)

        data = json.loads(request.body)

        try:
            email = data['email']
            username = data['username']
            info = data['info']
            password1 = data['password1']
            password2 = data['password2']
        except:
            return JsonResponse({
                "message": "Please enter all parameters ['email', 'username', 'info', 'password1', 'password2']"
            }, status=400)

        if password1 != password2:
            return JsonResponse({
                "message": "Password mismatch"
            }, status=400)

        try:
            user = User(email=email, username=username, info=info)
            user.set_password(password1)
            user.save()
        except:
            return JsonResponse({
                "message": "E-mail is does exists"
            })

        return JsonResponse({
            "message": "Success"
        }, status=200)

    def put(self, request, user_id=None):
        if user_id:
            data = json.loads(request.body)

            try:
                key = data['key']
            except:
                return JsonResponse({
                    "message": "Please input your api key"
                }, status=400)

            try:
                email = data['email']
            except:
                pass
            else:
                return JsonResponse({
                    "message": "Email does not change"
                }, status=400)

            username = data['username']
            info = data['info']
            password1 = data['password1']
            password2 = data['password2']

            if password1 != password2:
                return JsonResponse({
                    "message": "Password mismatch"
                }, status=400)
            try:
                user = User.objects.get(idx=user_id)
            except:
                return JsonResponse({
                    "message": f"user_id '{user_id}' is invalid user"
                }, status=404)

            user.username = username
            user.info = info
            user.set_password(password1)

            user.save()

            return JsonResponse({
                "message": "Success"
            }, status=200)
        else:
            return JsonResponse({
                "message": "Please enter a user_id"
            }, status=404)

    def delete(self, request, user_id=None):
        if user_id:
            data = json.loads(request.body)

            try:
                user = User.objects.get(idx=user_id)
            except:
                return JsonResponse({
                    "message": f"user_id '{user_id}' is invalid user"
                }, status=404)

            user.delete()

            return JsonResponse({
                "message": "Success"
            }, status=200)
        else:
            return JsonResponse({
                "message": "Please enter a user_id"
            }, status=404)