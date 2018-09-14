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