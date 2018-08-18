#/usr/bin/env python3
#coding=utf-8
import jenkins, socket

def job_init(func):
    def inner(self, **kwargs):
        print('func:%s is runing' % func.__name__)
        kwargs['server'] = self.init_server()
        print('kwargs: %s' % kwargs)
        return func(self, **kwargs)
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
        print('Now, %s from Jenkins .' % (current_user['fullName']))
        return server

    # 创建job工程
    @job_init
    def create_job(self,**kwargs):
        from ci.jenkins.jenkins_config_xml import job_config_xml
        if kwargs['config_xml']:
            JOB_CONFIG = job_config_xml(
                kwargs['config_xml']['description'],
                kwargs['config_xml']['url'],
                kwargs['config_xml']['credentialsId'],
                kwargs['config_xml']['BranchSpec'],
                kwargs['config_xml']['configName'],
                kwargs['config_xml']['remoteDirectory'],
                kwargs['config_xml']['sourceFiles'],
                kwargs['config_xml']['execCommand']
            ).get_config_xml()
            return kwargs['server'].create_job(name=kwargs['job_name'], config_xml=JOB_CONFIG)
        else:
            return kwargs['server'].create_job(name=kwargs['job_name'], config_xml=jenkins.EMPTY_CONFIG_XML)

    # 复制创建job工程
    @job_init
    def copy_job(self, **kwargs):
        kwargs['server'].copy_job(kwargs['job_name'], kwargs['copy_job_name'])
        return kwargs['server'].reconfig_job(name=kwargs['job_name'], config_xml=jenkins.RECONFIG_XML)

    # 查询所有job
    @job_init
    def get_jobs(self, **kwargs):
        # for job in jobs:
        #     print job['name']
        return kwargs['server'].get_jobs()

    #查询job配置
    @job_init
    def get_job_config(self, **kwargs):
        return kwargs['server'].get_job_config(name=kwargs['job_name'])

    #修改job配置
    @job_init
    def reconfig_job(self, **kwargs):
        return kwargs['server'].reconfig_job(name=kwargs['job_name'], config_xml=kwargs['config_xml'])

    #构建job工程
    @job_init
    def build_job(self, **kwargs):
        return kwargs['server'].build_job(name=kwargs['job_name'])

    # 查询job信息
    @job_init
    def get_job_info(self, **kwargs):
        return kwargs['server'].get_job_info(name=kwargs['job_name'])

    # 获取job最后构建number

    def get_lastBuildNumber(self, **kwargs):
        job_number = kwargs['server'].get_job_info(name=kwargs['job_name'])['lastBuild']['number']
        print('job_name: %s, lastBuildNumber : %s' % (kwargs['job_name'], job_number))
        return job_number

    # 获取job所有构建number
    def get_AllBuildNumber(self, **kwargs):
        job_number = kwargs['server'].get_job_info(name=kwargs['job_name'])['builds']
        job_list = []
        for job in job_number:
            job_list.append(job['number'])
        print('job_name: %s, AllBuildNumberList : %s' % (kwargs['job_name'], job_list))
        return job_list

    #暂停构建
    @job_init
    def stop_build(self, **kwargs):
        job_number = self.get_lastBuildNumber(**kwargs)
        return kwargs['server'].stop_build(name=kwargs['job_name'],number=job_number)

    # 删除当前job所有旧构建
    @job_init
    def delete_all_build(self, **kwargs):
        dict = {'status': True,'msg' : '暂未进行任何操作'}
        job_number_list = self.get_AllBuildNumber(**kwargs)
        delete_number_list = []
        current_job_number = self.get_lastBuildNumber(**kwargs)
        if job_number_list:
            for job_number in job_number_list:
                #查询是否为当前构建number
                if current_job_number != job_number:
                    kwargs['server'].delete_build(name=kwargs['job_name'], number=job_number)
                    delete_number_list.append(job_number)
            dict['msg'] = '该job：{}构建记录已删除'.format(delete_number_list)
        else:
            dict['status'] = False
            dict['msg'] = '该job不存在构建记录'
        return dict


    #删除job工作目录
    @job_init
    def wipeout_job_workspace(self, **kwargs):
        return kwargs['server'].wipeout_job_workspace(name=kwargs['job_name'])

    #获取构建信息
    @job_init
    def get_build_console_output(self, **kwargs):
        job_number = self.get_lastBuildNumber(**kwargs)
        return kwargs['server'].get_build_console_output(name=kwargs['job_name'],number=job_number)

    # 获取测试报告
    @job_init
    def get_build_console_output(self, **kwargs):
        job_number = self.get_lastBuildNumber(**kwargs)
        return kwargs['server'].get_build_test_report(name=kwargs['job_name'], number=job_number)

    #执行pipline Groovy脚本
    @job_init
    def run_script(self, **kwargs):
        return kwargs['server'].run_script(script_name=kwargs['script_name'])

    #添加插件
    @job_init
    def install_plugin(self, **kwargs):
        return kwargs['server'].install_plugin(name=kwargs['pluins_name'])

    #查询正在生成的列表
    @job_init
    def get_running_builds(self, **kwargs):
        return kwargs['server'].get_running_builds()

    #获取views列表
    @job_init
    def get_views(self, **kwargs):
        return kwargs['server'].get_views()




