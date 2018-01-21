#!/usr/bin/evn python
# -*- coding:utf-8 -*-
__author__ = 'Yuanzhi Bao'

from kingadmin.sites import site
from crm import models


site.register(models.UserProfile)
site.register(models.Role)