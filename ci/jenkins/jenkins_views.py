#/usr/bin/env python3
#coding=utf-8
from django.shortcuts import render,HttpResponse
from ci.jenkins.jenkins_utils import jenkins_tools

#添加job
def get_jobs(request):
    jk = jenkins_tools('http://10.100.99.151:8888/', 'huodong', '123456a')
    job_data = {
        'job_name' : 'test888',
        'job_info' : 'test123'
    }
    dd = jk.get_jobs(**job_data)
    job_list = []
    if dd:
        for job in dd['data']:
            job_list.append(job['name'])
    print(job_list)
    return HttpResponse(job_list)

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
    server = jenkins.Jenkins('http://10.100.99.151:8888/', username='huodong', password='123456a',
                             timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
    kk = server.delete_build('test888',6)
    print(kk)
    return HttpResponse(kk)





