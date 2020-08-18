# _*_ encoding:utf-8 _*_
# @Time : 2020/8/14 10:49
# @Author : chenmeihuan
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from user import views

urlpatterns = [
    path('hello/', views.hello),
    path('login/', views.login),
    path('api/login/', views.api_login),
    path('api/buglogs/', views.api_buglogs),
    path('home/', views.home)
]
