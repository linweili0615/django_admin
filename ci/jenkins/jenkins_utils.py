#/usr/bin/env python3
#coding=utf-8
import jenkins, socket, json, xmltodict
class jenkins_tools(object):
    def __init__(self, jenkins_url, username, password):
        self.jenkins_url = jenkins_url
        self.username = username
        self.password = password
        # jenkins_url = 'http://10.100.14.56:8888/'
        # username = 'huodong'
        # password = '123456a'

    #连接jenkins
    def init_server(self):
        server = jenkins.Jenkins(self.jenkins_url, username=self.username, password=self.password,
                                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        current_user = server.get_whoami()
        version = server.get_version()
        print('Now, %s from Jenkins %s.' % (current_user['fullName'], version))
        return server

    #查询job是否存在1
    def job_exists(self, job_name):
        # server = self.init_server()
        # print('get_job_info: %s' % server.get_job_info(name=job_name))
        return self.init_server().job_exists(name=job_name)

    #查询job信息
    def get_job_info(self, job_name):
        # server = self.init_server()
        # print('get_job_info: %s' % server.get_job_info(name=job_name))
        info = self.init_server().get_job_info(name=job_name)
        # print(type(info))
        return json.dumps(info)

    #查询job配置
    def get_job_config(self, job_name):
        info = self.init_server().get_job_config(name=job_name)
        return json.dumps(info)

    #查询所有job列表
    def get_jobs(self):
        return self.init_server().get_jobs()

    #构建job
    def build_job(self, job_name):
        return self.init_server().build_job(name=job_name)

    #暂停构建job
    def stop_build(self, job_name, num):
        return self.init_server().stop_build(name=job_name,number=num)

    #删除job工作目录
    def wipeout_job_workspace(self, job_name):
        return self.init_server().wipeout_job_workspace(job_name)

    def get_build_console_output(self,job_name,num):
        return self.init_server().get_build_console_output(name=job_name,number=num)