#!/usr/bin/env python
#coding=utf-8
#*************************************************
#
#       Filename: website/urls.py
#         Author: mocoslee
#          Email: mocoslee@gmail.com
#         Create: 2017-10-14 20:10:56
#    Description: -
#
#*************************************************
from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^baseshow/$',views.BaseShow.as_view(),name = 'baseshow'),
]
