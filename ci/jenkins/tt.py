#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
jk = Jenkins('http://localhost:8080/', username='linweili', password='123456a')
# print(jk.keys())
import json
import dicttoxml
def get_normal_config(**kwargs):
    import os
    with open('jenkins_config.json', 'r', encoding='utf-8') as f:
        normal_config = json.load(f)
    # print('normal_config: %s' % normal_config)
    # print('kwargs: %s' % kwargs)
    # description
    normal_config['maven2-moduleset']['description'] = kwargs['description']
    # git_url
    normal_config['maven2-moduleset']['scm']['userRemoteConfigs'][
        'hudson.plugins.git.UserRemoteConfig']['url'] = kwargs['git_url']
    # git_branches
    normal_config['maven2-moduleset']['properties']['hudson.model.ParametersDefinitionProperty'][
        'parameterDefinitions'][
        'com.gem.persistentparameter.PersistentStringParameterDefinition']['defaultValue'] = kwargs['git_branches']
    # ssh
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers'][
        'jenkins.plugins.publish__over__ssh.BapSshPublisher']['configName'] = kwargs['ssh']
    # remotedirectory
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['remoteDirectory'] = kwargs['remotedirectory']
    # sourcefiles
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['sourceFiles'] = kwargs['sourcefiles']
    # execcommand
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['execCommand'] = kwargs['execcommand']

    xml = dicttoxml.dicttoxml(normal_config).decode(encoding='utf-8')
    # print(type(xml))
    print(xml)
    return xml
args = {
        'description' : '测试下这个问题',
        'git_url' : 'https://github.com/linweili0615/testsearch.git',
        'git_branches' : '*/master',
        'ssh' : 'test1234',
        'remotedirectory' : 'source/test',
        'sourcefiles' : '**/target/demo-2.0.jar',
        'execcommand' : 'sh /usr/local/software/test3.sh test demo-1.0.jar 9301'
    }

config_xml = get_normal_config(**args)
jk.create_job('test999', xml = config_xml)