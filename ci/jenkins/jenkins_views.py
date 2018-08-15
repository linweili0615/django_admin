#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
import socket, jenkins

def get_jenkins_status(request):
    jenkins_url = 'http://10.100.14.56:8888/'
    username = 'huodong'
    password = '123456a'
    server = jenkins.Jenkins(jenkins_url, username=username, password=password,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
    current_user = server.get_whoami()
    version = server.get_version()
    print('Now, %s from Jenkins %s.' % (current_user['fullName'], version ))
    return HttpResponse('ok')

def get_job_status(request):
    return HttpResponse('ok')

def create_job(request):
    return

def copy_job(request):
    return

def delete_job(request):
    return

def build_job(request):
    return




def get_jobs(request):
    return



