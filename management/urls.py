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
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy
from mcms.nav import *
from . import views

urlpatterns = [
	url(r'^dashboard/$',views.DashBoard.as_view(),name = 'dashboard'),
	url(r'^test/$',views.TestC.as_view(),name = 'test'),
]

test = SidebarItem(reverse_lazy('management:test'),"test","fa","")
nav_manager.add_sidebar_item("",_(u'test'),"fa",[test])
