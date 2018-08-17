#/usr/bin/env python3
#coding=utf-8
import jenkins, socket, json
from ci import result_data


def job_exists(func):
    def inner(self, **kwargs):
        print('job_exists:kwargs: %s' % kwargs)
        jenkins_server = self.init_server()
        try:
            print('%s is runing' % func.__name__)
            kwargs['server'] = jenkins_server
            print('kwargs: %s' % kwargs)
            return func(self, **kwargs)
        except jenkins.JenkinsException:
            print('job: %s exists' % kwargs['job_name'])
            return False
    return inner

class jenkins_tools(object):
    def __init__(self, jenkins_url, username, password):
        self.jenkins_url = jenkins_url
        self.username = username
        self.password = password

    #获取jenkins连接
    def init_server(self):
        server = jenkins.Jenkins(self.jenkins_url, username=self.username, password=self.password,
                                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        current_user = server.get_whoami()
        version = server.get_version()
        print('Now, %s from Jenkins %s.' % (current_user['fullName'], version))
        return server

    # 创建job工程
    @job_exists
    def create_job(self,**kwargs):
        print('create_job:kwargs %s' % kwargs)
        return kwargs['server'].create_job(name=kwargs['job_name'], config_xml=kwargs['job_info'])

    # #检查job是否存在
    # def job_exists(self, server):
    #     def assert_job(job_name):
    #         print('job_name:%s'% job_name)
    #         return server.job_exists(name=job_name)
    #     return assert_job

    #查询job信息
    def get_job_info(self, job_name):
        return self.init_server().get_job_info(name=job_name)

    # 查询所有job列表
    def get_info(self):
        return self.init_server().get_info()

    #获取job最后构建number
    def get_lastBuildNumber(self, job_name):
        return self.get_job_info(job_name)['lastCompletedBuild']['number']

    #查询job配置
    def get_job_config(self, job_name):
        server = self.init_server()
        job = self.job_exists(server)
        status = job(job_name)
        # print('status: %s' % status)
        if status:
            return self.init_server().get_job_config(name=job_name)
        else:
            print('%s : job 不存在' % job_name)
            return False,'%s : job 不存在' % job_name




    #修改job配置
    def reconfig_job(self, job_name, job_info):
        return self.init_server().reconfig_job(name=job_name, config_xml=job_info)

    #构建job工程
    def build_job(self, job_name):
        server = self.init_server()
        job = self.job_exists(server)
        status = job(job_name)
        if status:
            return server.build_job(name=job_name)
        else:
            print('%s : job 不存在' % job_name)
            return False,'%s : job 不存在' % job_name

    #暂停构建
    def stop_build(self, job_name, job_num):
        return self.init_server().stop_build(name=job_name,number=job_num)
    
    #删除构建
    def delete_build(self, job_name, job_num):
        return self.init_server().delete_build(name=job_name, number=job_num)

    #删除job工作目录
    def wipeout_job_workspace(self, job_name):
        return self.init_server().wipeout_job_workspace(job_name)

    #获取构建信息
    def get_build_console_output(self,job_name,job_num):
        return self.init_server().get_build_console_output(name=job_name,number=job_num)

    # 获取测试报告
    def get_build_console_output(self, job_name, job_num):
        return self.init_server().get_build_test_report(name=job_name, number=job_num)

    #执行pipline Groovy脚本
    def run_script(self, script):
        return self.init_server().run_script(script)

    #添加插件
    def install_plugin(self, pluins_name):
        return  self.init_server().install_plugin(pluins_name)

    #查询正在生成的列表
    def get_running_builds(self):
        return self.init_server().get_running_builds()

    #获取views列表
    def get_views(self):
        return self.init_server().get_views()




