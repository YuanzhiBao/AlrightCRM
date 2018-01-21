#!/usr/bin/evn python
# -*- coding:utf-8 -*-
__author__ = 'Yuanzhi Bao'

from django.shortcuts import render, HttpResponse

#import every kingadmin in every app
from kingadmin.app_setup import discover
discover()
from kingadmin.sites import site

print(site.enabledadmin)


def dashboard(request):
    return render(request, "kingadmin/showdata.html", {"sites": site.enabledadmin})

def table_list(request, app_name, model_name):

    table_model = site.enabledadmin[app_name][model_name].model
    queryset = table_model.objects.all()
    print(queryset)
    return render(request, "kingadmin/table_list.html", {"queryset": queryset})

