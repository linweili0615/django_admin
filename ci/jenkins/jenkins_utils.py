#/usr/bin/env python3
#coding=utf-8
import jenkins, socket
class jenkins_tools(object):
    def __init__(self, jenkins_url, username, password):
        self.jenkins_url = jenkins_url
        self.username = username
        self.password = password
        # jenkins_url = 'http://10.100.14.56:8888/'
        # username = 'huodong'
        # password = '123456a'

    def init_server(self):
        server = jenkins.Jenkins(self.jenkins_url, username=self.username, password=self.password,
                                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        current_user = server.get_whoami()
        version = server.get_version()
        print('Now, %s from Jenkins %s.' % (current_user['fullName'], version))
        return server