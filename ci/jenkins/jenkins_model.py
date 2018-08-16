#/usr/bin/env python3
#coding=utf-8
from django.db import models

class jenkins_info(models.Model):
    url = models.CharField(max_length=50,primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)