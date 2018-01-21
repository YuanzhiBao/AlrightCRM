#!/usr/bin/evn python
# -*- coding:utf-8 -*-
__author__ = 'Yuanzhi Bao'

from kingadmin.baseadmin import Admin_Base

class CustomAdmin(Admin_Base):


    def __init__(self):
        self.enabledadmin = {}

    def register(self, model_class, admin_class=None):
        app_name = model_class._meta.app_label
        model_name = model_class._meta.model_name
        if not admin_class:
            admin_class = Admin_Base()
        else:
            admin_class = admin_class()
        admin_class.model = model_class

        if app_name not in self.enabledadmin:
            self.enabledadmin[app_name] = {}
        self.enabledadmin[app_name][model_name] = admin_class


site = CustomAdmin()
