#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
from ci.jenkins.jenkins_utils import jenkins_tools
from ci.jenkins.utils import jobs_info_dict
import json

#获取job列表
def get_jobs_list(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    jobs = jk.get_jobs()
    jobs_list = []
    for cc in jobs['data']:
        jobs_list.append(cc['name'])
    return HttpResponse(json.dumps({'jobs_list':jobs_list}))
#添加job
def create_job(request):
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    # jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    args = {
        'name' : 'test999',
        'config_xml':{
            'description': '测试下这个问题',
            'git_url': 'http://git.tuandai888.com/user/user-service-admin.git',
            'git_branches': '*/Feature/sqlExecute_20180912',
            'ssh': '10.100.14.5',
            'remotedirectory': 'source_code/user-service-admin',
            'sourcefiles': '**/target/user-service-admin-1.0-SNAPSHOT.jar',
            'execcommand': 'echo "hello"'
        }

    }
    info = jk.create_job(**args)
    return HttpResponse(json.dumps({'info':info},ensure_ascii=False))
#修改job配置
def reconfig_job(request):
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    # jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    args = {
        'name' : 'test999',
        'config_xml':{
            'description': '测试下这个问题',
            'git_url': 'http://git.tuandai888.com/user/user-service-admin.git',
            'git_branches': '*/Feature/sqlExecute_20180912',
            'ssh': '10.100.14.5',
            'remotedirectory': 'source_code/user-service-admin',
            'sourcefiles': '**/target/user-service-admin-1.0-SNAPSHOT.jar',
            'execcommand': 'echo "hello"'
        }

    }
    info = jk.reconfig_job(**args)
    return HttpResponse(json.dumps({'info':info},ensure_ascii=False))
#参数化构建
def build_job_by_params(request):
    # jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    job = jk.build_job(**{
        'name': 'test999',
        'parameters':{
            'branch': '*/develop'
        }
    })
    return HttpResponse(json.dumps({'job_num':job['data'],'msg':job['msg']}, ensure_ascii=False))

def get_job_config(request):
    # jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    config = jk.get_job_config(**{'name': 'test999'})['data']
    # print('config_xml: %s' % config)
    from ci.jenkins.jenkins_utils import xmltojson
    config_data = xmltojson(config)
    jobs_info_json = json.dumps(jobs_info_dict(config_data),ensure_ascii=False)
    print(jobs_info_json)
    return HttpResponse(jobs_info_json)

#添加job
def get_all_jobs_info(request):
    # jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    jobs_info = jk.get_all_jobs_info()
    jobs_info_target = {}
    for key in jobs_info['data']:
        jobs_info_target[key] = jobs_info_dict(jobs_info['data'][key])
    jobs_info_json = json.dumps(jobs_info)
    print(jobs_info_json)
    return HttpResponse(jobs_info_json)

def get_last_build(request):
    jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    # jk = jenkins_tools('http://10.100.99.151:8888/', 'huodong', '123456a')
    lastBuild = jk.get_lastBuild(**{'name':'test'})
    return HttpResponse(json.dumps({'lastBuild':lastBuild},ensure_ascii=False))








