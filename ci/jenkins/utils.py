#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def jobs_info_dict(config_data):
    print('jobs_info_dict: %s' % config_data)
    desc = config_data['maven2-moduleset']['description']
    print('desc: %s' % desc)
    git_url = config_data['maven2-moduleset']['scm']['userRemoteConfigs']['hudson.plugins.git.UserRemoteConfig']['url']
    git_branches = config_data['maven2-moduleset']['scm']['branches']['hudson.plugins.git.BranchSpec']['name']
    target_server = config_data['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['configName']
    remote_directory = config_data['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers']['jenkins.plugins.publish__over__ssh.BapSshTransfer']['remoteDirectory']
    sourcefiles = config_data['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers']['jenkins.plugins.publish__over__ssh.BapSshTransfer']['sourceFiles']
    exec_command = config_data['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers']['jenkins.plugins.publish__over__ssh.BapSshTransfer']['execCommand']
    return {
        'desc' : desc,
        'git_url': git_url,
        'git_branches': git_branches,
        'target_server': target_server,
        'remote_directory': remote_directory,
        'sourcefiles': sourcefiles,
        'exec_command': exec_command
    }

def get_xml():
    import xml.etree.ElementTree as ET
    tree = ET.parse('jenkins_normal_config.xml')
    print('tree: %s' % tree.getiterator())

if __name__ == '__main__':
    import json
    with open('jenkins_config.json', 'r', encoding='utf-8') as f:
        normal_config = json.load(f)
    # description
    normal_config['maven2-moduleset']['description'] = ''
    # git_url
    normal_config['maven2-moduleset']['scm']['userRemoteConfigs'][
        'hudson.plugins.git.UserRemoteConfig']['url'] = ''
    # git_branches
    normal_config['maven2-moduleset']['properties']['hudson.model.ParametersDefinitionProperty']['parameterDefinitions'][
        'com.gem.persistentparameter.PersistentStringParameterDefinition']['defaultValue'] = ''
    # SSH
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin']['delegate']['delegate'][
        'publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['configName'] = ''
    # remoteDirectory
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['remoteDirectory'] = ''
    # sourceFiles
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['sourceFiles'] = ''
    # execCommand
    normal_config['maven2-moduleset']['postbuilders']['jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin'][
        'delegate']['delegate']['publishers']['jenkins.plugins.publish__over__ssh.BapSshPublisher']['transfers'][
        'jenkins.plugins.publish__over__ssh.BapSshTransfer']['execCommand'] = ''
    import dicttoxml
    xml = dicttoxml.dicttoxml(normal_config).decode(encoding='utf-8')
    print(type(xml))
    print(xml)

    #保存文件
    # file = open('test.json', 'w', encoding='utf-8')
    # data1 = {'name': '中文', "age": 12}
    # data2 = {'name': 'merry', "age": 13}
    # data = [data1, data2]
    # print(data)
    # json.dump(data, file, ensure_ascii=False)
    # file.close()
