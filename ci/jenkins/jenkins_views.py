#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
from ci.jenkins.jenkins_utils import jenkins_tools
from ci.jenkins.utils import jobs_info_dict
import json

def get_jobs_list(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    jobs = jk.get_jobs()
    jobs_list = []
    for cc in jobs['data']:
        jobs_list.append(cc['name'])
    return HttpResponse(json.dumps({'jobs_list':jobs_list}))

def build_job_by_params(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    job = jk.build_job(**{
        'name': 'test',
        'parameters':{
            'branch': '*/'+'master'
        }
    })
    return HttpResponse(json.dumps({'job_num':job['data'],'msg':job['msg']}, ensure_ascii=False))

def get_job_config(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    config = jk.get_job_config(**{'name': 'test'})['data']
    print('config_xml: %s' % config)
    from ci.jenkins.jenkins_utils import xmltojson
    config_data = xmltojson(config)
    jobs_info_json = json.dumps(jobs_info_dict(config_data),ensure_ascii=False)
    print(jobs_info_json)
    return HttpResponse(jobs_info_json)

#添加job
def get_all_jobs_info(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    jobs_info = jk.get_all_jobs_info()
    jobs_info_target = {}
    for key in jobs_info['data']:
        jobs_info_target[key] = jobs_info_dict(jobs_info['data'][key])
    jobs_info_json = json.dumps(jobs_info)
    print(jobs_info_json)
    return HttpResponse(jobs_info_json)

#添加job
def create_job(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.99.151:8888/', 'huodong', '123456a')
    job_data = {

    }
    dd = jk.create_job(**job_data)
    print(dd)
    return HttpResponse(dd)

def get_last_build(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.99.151:8888/', 'huodong', '123456a')
    lastBuild = jk.get_lastBuild(**{'name':'test'})
    return HttpResponse(json.dumps({'lastBuild':lastBuild},ensure_ascii=False))

def get_all_jobs_info(request):
    jk = jenkins_tools('http://10.100.14.56:8888/', 'huodong', '123456a')
    job_data = {
        'job_name': 'hd-thirdplat-landing-web-9',
        'job_info': 'test123'
    }
    jobs = jk.get_jobs(**job_data)
    joblist = []
    for job in jobs['data']:
        joblist.append(job['name'])
    job_list_info = {}
    for jb in joblist:
        job_data['job_name'] = jb
        job_list_info[jb] = (jk.get_job_info(**job_data)['data'])

    job_list_config = {}

    for jb in joblist:
        job_data['job_name'] = jb
        job_list_config[jb] = (jk.get_job_config(**job_data)['data'])
    print(job_list_info)
    print(job_list_config)
    return HttpResponse(job_list_info)





