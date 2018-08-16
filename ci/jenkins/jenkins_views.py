#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
from ci.jenkins.jenkins_utils import jenkins_tools

#添加job
def create_job(request):
    jk = jenkins_tools('http://10.100.14.56:8888/', 'huodong', '123456a')
    # dd= jk.job_exists('activity-web-52')
    dd = jk.wipeout_job_workspace('activity-web-52')
    # dd = jk.get_jobs()
    print(dd)
    return HttpResponse(dd)


