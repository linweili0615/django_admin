#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
from ci.jenkins.jenkins_utils import jenkins_tools

#添加job
def create_job(request):
    jk = jenkins_tools('http://10.100.14.56:8888/', 'huodong', '123456a')
    server = jk.init_server()
    return HttpResponse(server.get_version())


