from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.http import  JsonResponse, HttpResponse
from .models import User, SubUser
from .status_code import HTTP_201_CREATED




@require_http_methods(["GET", "POST"])
@csrf_exempt
def user(request):
    """Method for creating or retrieving users"""
    if request.method == "POST":
        profile_data = json.loads(request.body)
        new_user = User(**profile_data)
        new_user.save()

        return JsonResponse(model_to_dict(new_user), status=HTTP_201_CREATED)

    all_users = User.objects.all().values('username','first_name', 'last_name','email')
    return JsonResponse(list(all_users), safe=False)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def sub_user(request):
    """Method for creating or retrieving sub users"""
    if request.method == "POST":
        profile_data = json.loads(request.body)
        new_subuser = SubUser(**profile_data)
        new_subuser.save()

        return JsonResponse(model_to_dict(new_subuser), status=HTTP_201_CREATED)

    all_subusers = SubUser.objects.all().values('username','first_name', 'last_name','email')
    return JsonResponse(list(all_subusers), safe=False)