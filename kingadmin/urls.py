#!/usr/bin/evn python
# -*- coding:utf-8 -*-
__author__ = 'Yuanzhi Bao'


from django.urls import path, include
from django.conf.urls import url
from kingadmin import views

urlpatterns = [
    url(r'^(\w+)/(\w+)/$',views.table_list, name="table_list"),
    url(r'^$',views.dashboard)
]