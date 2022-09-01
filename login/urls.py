from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('',views.home,name="home"),
    path('result/',views.result,name="result"),
    path('create/', GetView.as_view()),
    path('uploadapi/', UploadView.as_view()),
    path('login/',views.login,name="login"),
    path('login_result/',views.login_result,name="login_result"),
    path('upload/',views.upload,name="upload"),
]

