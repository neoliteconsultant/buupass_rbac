from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import User, SubUser
from .status_code import HTTP_201_CREATED


@require_http_methods(["GET", "POST"])
def user(request):
    """Method for creating or retrieving users"""
    if request.method == "POST":
        new_user = User(request.body)
        new_user.save()

        return JsonResponse(new_user, safe=False, status=HTTP_201_CREATED)

    all_users = User.objects.all()
    return JsonResponse(all_users, safe=False)


@require_http_methods(["GET", "POST"])
def sub_user(request):
    """Method for creating or retrieving sub users"""
    if request.method == "POST":
        new_subuser = SubUser(request.body)
        new_subuser.save()

        return JsonResponse(new_subuser, safe=False, status=HTTP_201_CREATED)

    all_subusers = SubUser.objects.all()
    return JsonResponse(all_subusers, safe=False)