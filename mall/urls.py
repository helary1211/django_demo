# _*_ encoding:utf-8 _*_
# @Time : 2020/8/13 19:40
# @Author : chenmeihuan
# @File : urls.py
# @Software: PyCharm

from django.contrib import admin
from django.urls import path
from mall import views

urlpatterns = [
    path('hello/', views.hello),
]
