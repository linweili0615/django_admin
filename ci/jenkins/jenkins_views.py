#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
from ci.jenkins.jenkins_utils import jenkins_tools
import json

def get_jobs_list(request):
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    jobs = jk.get_jobs()
    jobs_list = []
    for cc in jobs['data']:
        jobs_list.append(cc['name'])
    # print(jobs_list)
    return HttpResponse(json.dumps({'jobs_list':jobs_list}))

def build_job_by_params(request):
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    job = jk.build_job(**{
        'name': 'test',
        'parameters':{
            'branch': 'develop'
            # 'branch': '*/Feature/pcLoginPageAdjuest_20180830'
        }
    })
    return HttpResponse(json.dumps({'job_num':job['data'],'msg':job['msg']}))

def get_job_config(request):
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    config = jk.get_job_config(**{'job_name': 'activity-query-service-5'})['data']
    from ci.jenkins.jenkins_utils import xmltojson
    config_data = xmltojson(config)
    git_url = \
        config_data['maven2-moduleset']['scm']['userRemoteConfigs']['hudson.plugins.git.UserRemoteConfig']['url']
    git_branches = config_data['maven2-moduleset']['scm']['branches']['hudson.plugins.git.BranchSpec'][
        'name']
    target_server = config_data['maven2-moduleset']['postbuilders'][
        'jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers'][
        'jenkins.plugins.publish__over__ssh.BapSshPublisher']['configName']
    remote_directory = config_data['maven2-moduleset']['postbuilders'][
        'jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers'][
        'jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['remoteDirectory']
    sourcefiles = config_data['maven2-moduleset']['postbuilders'][
        'jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers'][
        'jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['sourceFiles']
    exec_command = config_data['maven2-moduleset']['postbuilders'][
        'jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers'][
        'jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['execCommand']
    jobs_info_dict = {
        'git_url': git_url,
        'git_branches': git_branches,
        'target_server': target_server,
        'remote_directory': remote_directory,
        'sourcefiles': sourcefiles,
        'exec_command': exec_command
    }

    jobs_info_json = json.dumps(jobs_info_dict)
    print(jobs_info_json)
    return HttpResponse(jobs_info_json)

#添加job
def get_all_jobs_info(request):
    # jk = jenkins_tools('http://localhost:8080/', 'linweili', '123456a')
    jk = jenkins_tools('http://10.100.14.134:8080/', 'jenkins888', '123456a')
    jobs_info = jk.get_all_jobs_info()
    jobs_info_dict = {}
    for key in jobs_info['data']:

        git_url = jobs_info['data'][key]['maven2-moduleset']['scm']['userRemoteConfigs']['hudson.plugins.git.UserRemoteConfig']['url']
        git_branches = jobs_info['data'][key]['maven2-moduleset']['scm']['branches']['hudson.plugins.git.BranchSpec']['name']
        target_server = jobs_info['data'][key]['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['configName']
        remote_directory = jobs_info['data'][key]['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers']['jenkins.plugins.publish__over__ssh.BapSshTransfer']['remoteDirectory']
        sourcefiles = jobs_info['data'][key]['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers']['jenkins.plugins.publish__over__ssh.BapSshTransfer']['sourceFiles']
        exec_command = jobs_info['data'][key]['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers']['jenkins.plugins.publish__over__ssh.BapSshTransfer']['execCommand']

    jobs_info_dict[key] = {
            'git_url' : git_url,
            'git_branches' : git_branches,
            'target_server' : target_server,
            'remote_directory' : remote_directory,
            'sourcefiles' : sourcefiles,
            'exec_command' : exec_command
        }

    jobs_info_json = json.dumps(jobs_info_dict)
    print(jobs_info_json)
    return HttpResponse(jobs_info_json)

#添加job
def create_job(request):
    jk = jenkins_tools('http://10.100.99.151:8888/', 'huodong', '123456a')
    job_data = {
        'job_name' : 'test_jenkins',
        'config_xml' : {
            'description' : '七夕qixiFestival2018',
            'url' : 'http://git.tuandai888.com/td-services/activity-web.git',
            'credentialsId' : '2c8de544-7812-4478-b0e9-04c17ddca5ac',
            'BranchSpec' : '*/dev_settle_zx',
            'configName' : '10.100.14.52',
            'remoteDirectory' : 'source_code/activity-web',
            'sourceFiles' : '**/web /target/activity-website-0.0.1-SNAPSHOT.jar',
            'execCommand' : 'sh /usr/local/deploy/update_module-web.sh activity-web activity-website-0.0.1-SNAPSHOT.jar 9308'
        }
    }
    dd = jk.create_job(**job_data)
    print(dd)
    return HttpResponse(dd)

#添加job
def get_lastBuildNumber(request):
    import jenkins, socket
    server = jenkins.Jenkins('http://10.100.14.56:8888/', username='huodong', password='123456a',
                             timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
    kk = server.get_all_jobs()
    # kk = server.delete_build('test888',6)
    print(kk)
    return HttpResponse(kk)

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





