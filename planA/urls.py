from django.contrib import admin
from django.urls import re_path, include
from planA import views
urlpatterns = [
    re_path(r'^plan', views.GetUserTime.as_view(), name='return-user-time'),
]
