from django.urls import path

from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('sub_user', views.sub_user, name='sub_user'),
]