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
        try:
            server = jenkins.Jenkins(self.jenkins_url, username=self.username, password=self.password,
                                     timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
            current_user = server.get_whoami()
            print('Now, %s from Jenkins .' % (current_user['fullName']))
            return server
        except:
            print('获取Jenkins连接信息失败')
            return None


    # 创建job工程
    @job_init
    def create_job(self,**kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        from ci.jenkins.jenkins_config_xml import job_config_xml
        if kwargs['config_xml']:
            job_config = job_config_xml(
                kwargs['config_xml']['description'],
                kwargs['config_xml']['url'],
                kwargs['config_xml']['credentialsId'],
                kwargs['config_xml']['BranchSpec'],
                kwargs['config_xml']['configName'],
                kwargs['config_xml']['remoteDirectory'],
                kwargs['config_xml']['sourceFiles'],
                kwargs['config_xml']['execCommand']
            ).get_config_xml()
            try:
                kwargs['server'].create_job(name=kwargs['job_name'], config_xml=job_config)
                dict['msg'] = '添加job成功'
                return dict
            except:
                dict['status'] = False
                dict['msg'] = '添加job成功失败'
                return dict
        else:
            try:
                kwargs['server'].create_job(name=kwargs['job_name'], config_xml=jenkins.EMPTY_CONFIG_XML)
                dict['msg'] = '添加空白job成功'
                return dict
            except:
                dict['status'] = False
                dict['msg'] = '添加空白job失败'
                return dict

    # 复制创建job工程
    @job_init
    def copy_job(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].copy_job(kwargs['job_name'], kwargs['copy_job_name'])
            dict['msg'] = '复制job工程成功'
            kwargs['server'].reconfig_job(name=kwargs['job_name'], config_xml=jenkins.RECONFIG_XML)
            dict['msg'] = '复制job工程修改配置文件成功'
            return dict
        except:
            dict['status'] = False
            dict['msg'] = '复制创建job工程失败'
            return dict

    # 查询所有job[0]['name']
    @job_init
    def get_jobs(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].get_jobs()
            dict['msg'] = '查询所有job名称成功'
            return dict
        except:
            dict['msg'] = '查询所有job名称失败'
            dict['status'] = False
            return dict

    #查询job配置
    @job_init
    def get_job_config(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].get_job_config(name=kwargs['job_name'])
            dict['msg'] = '查询job配置成功'
            return dict
        except:
            dict['msg'] = '查询job配置失败'
            dict['status'] = False
            return dict

    #修改job配置
    @job_init
    def reconfig_job(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        from ci.jenkins.jenkins_config_xml import job_config_xml
        if kwargs['config_xml']:
            job_config = job_config_xml(
                kwargs['config_xml']['description'],
                kwargs['config_xml']['url'],
                kwargs['config_xml']['credentialsId'],
                kwargs['config_xml']['BranchSpec'],
                kwargs['config_xml']['configName'],
                kwargs['config_xml']['remoteDirectory'],
                kwargs['config_xml']['sourceFiles'],
                kwargs['config_xml']['execCommand']
            ).get_config_xml()
            try:
                kwargs['server'].reconfig_job(name=kwargs['job_name'], config_xml=job_config)
                dict['msg'] = '修改job工程配置文件成功'
                return dict
            except:
                dict['msg'] = '修改job工程配置文件失败'
                dict['status'] = False
                return dict
        else:
            dict['msg'] = '修改job工程配置文件为空'
            dict['status'] = False
            return dict

    #构建job工程
    @job_init
    def build_job(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].build_job(name=kwargs['job_name'])
            dict['msg'] = '构建job成功'
            return dict
        except:
            dict['msg'] = '构建job失败'
            dict['status'] = False
            return dict

    # 查询job信息
    @job_init
    def get_job_info(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].get_job_info(name=kwargs['job_name'])
            dict['msg'] = '获取job信息成功'
            return dict
        except:
            dict['msg'] = '获取job信息失败'
            dict['status'] = False
            return dict

    # 获取job最后构建number
    def get_lastBuildNumber(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            job_number = kwargs['server'].get_job_info(name=kwargs['job_name'])['lastBuild']['number']
            print('job_name: %s, lastBuildNumber : %s' % (kwargs['job_name'], job_number))
            dict['msg'] = job_number
            return dict
        except:
            dict['msg'] = '获取当前job最后构建number失败'
            dict['status'] = False
            return dict

    # 获取job所有构建number
    def get_AllBuildNumber(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            job_number = kwargs['server'].get_job_info(name=kwargs['job_name'])['builds']
            job_list = []
            for job in job_number:
                job_list.append(job['number'])
            print('job_name: %s, AllBuildNumberList : %s' % (kwargs['job_name'], job_list))
            dict['msg'] = job_list
            return dict
        except:
            dict['msg'] = '获取当前job所有构建number失败'
            dict['status'] = False
            return dict

    #暂停构建
    @job_init
    def stop_build(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        job_number = self.get_lastBuildNumber(**kwargs)
        try:
            if job_number['status']:
                kwargs['server'].stop_build(name=kwargs['job_name'],number=job_number['msg'])
            else:
                dict['msg'] = job_number['msg']
                dict['status'] = False
                return dict
        except:
            dict['msg'] = '暂停构建失败'
            dict['status'] = False
            return dict

    # 删除当前job所有旧构建
    @job_init
    def delete_all_build(self, **kwargs):
        dict = {'status': True,'msg' : '暂未进行任何操作'}
        job_number_list = self.get_AllBuildNumber(**kwargs)
        delete_number_list = []
        current_job_number = self.get_lastBuildNumber(**kwargs)
        if job_number_list['status']:
            for job_number in job_number_list['msg']:
                #查询是否为当前构建number
                if current_job_number['msg'] != job_number:
                    try:
                        kwargs['server'].delete_build(name=kwargs['job_name'], number=job_number)
                        delete_number_list.append(job_number)
                        dict['msg'] = '删除当前job所有旧构建成功'
                    except:
                        dict['status'] = False
                        dict['msg'] = '删除当前job所有旧构建失败'
                        return dict
            dict['msg'] = '该job：{}构建记录已删除'.format(delete_number_list)
            return dict
        else:
            dict['status'] = False
            dict['msg'] = job_number_list['msg']
            return dict


    #删除当前job工作目录
    @job_init
    def wipeout_job_workspace(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].wipeout_job_workspace(name=kwargs['job_name'])
            dict['msg'] = '删除job工作目录成功'
            return dict
        except:
            dict['status'] = False
            dict['msg'] = '删除job工作目录失败'
            return dict

    #获取job构建信息
    @job_init
    def get_build_console_output(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        job_number = self.get_lastBuildNumber(**kwargs)
        if job_number['status']:
            try:
                kwargs['server'].get_build_console_output(name=kwargs['job_name'], number=job_number)
                dict['msg'] = '获取job构建信息'
                return dict
            except:
                dict['status'] = False
                dict['msg'] = '获取job构建信息失败'
                return dict
        else:
            dict['status'] = False
            dict['msg'] = job_number['msg']
            return dict

    # 获取测试报告
    @job_init
    def get_build_console_output(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        job_number = self.get_lastBuildNumber(**kwargs)
        if job_number['status']:
            try:
                kwargs['server'].get_build_test_report(name=kwargs['job_name'], number=job_number)
                dict['msg'] = '获取测试报告成功'
                return dict
            except:
                dict['msg'] = '获取测试报告失败'
                return dict
        else:
            dict['msg'] = job_number['msg']
            dict['status'] = False
            return dict

    #pipline  执行Groovy脚本
    @job_init
    def run_script(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].run_script(script_name=kwargs['script_name'])
            dict['msg'] = '执行Groovy脚本成功'
            return dict
        except:
            dict['msg'] = '执行Groovy脚本失败'
            dict['status'] = False
            return dict

    #添加插件
    @job_init
    def install_plugin(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].install_plugin(name=kwargs['pluins_name'])
            dict['msg'] = '添加插件成功'
            return dict
        except:
            dict['添加插件失败']
            dict['status'] = False
            return dict

    #查询正在构建的列表
    @job_init
    def get_running_builds(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].get_running_builds()
            dict['msg'] = '查询正在构建的列表成功'
            return dict
        except:
            dict['msg'] = '查询正在构建的列表失败'
            dict['status'] = False
            return dict

    #获取views列表
    @job_init
    def get_views(self, **kwargs):
        dict = {'status': True, 'msg': '暂未进行任何操作'}
        try:
            kwargs['server'].get_views()
            dict['msg'] = '获取views列表成功'
            return dict
        except:
            dict['msg'] = '获取views列表失败'
            dict['status'] = False
            return dict




