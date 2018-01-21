#!/usr/bin/evn python
# -*- coding:utf-8 -*-
__author__ = 'Yuanzhi Bao'

from django import conf
import importlib

def discover():
    for item in conf.settings.INSTALLED_APPS:
        try:
            importlib.__import__("%s.kingadmin" % item)
        except Exception:
            pass