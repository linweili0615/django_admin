#/usr/bin/env python3
#coding=utf-8


class job_config_xml(object):
    def __init__(self, description, url, credentialsId, BranchSpec, configName, remoteDirectory, sourceFiles, execCommand):
        self.description = description
        self.url = url
        self.credentialsId = credentialsId
        self.BranchSpec = BranchSpec
        self.configName = configName
        self.remoteDirectory = remoteDirectory
        self.sourceFiles = sourceFiles
        self.execCommand = execCommand

    def get_config_xml(self):
        CONFIG_XML = '''
<?xml version='1.1' encoding='UTF-8'?>
<maven2-moduleset plugin="maven-plugin@3.1.2">
    <description>{}</description>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.plugins.git.GitSCM" plugin="git@3.9.1">
        <configVersion>2</configVersion>
        <userRemoteConfigs>
            <hudson.plugins.git.UserRemoteConfig>
                <url>{}</url>
                <credentialsId>{}</credentialsId>
            </hudson.plugins.git.UserRemoteConfig>
        </userRemoteConfigs>
        <branches>
            <hudson.plugins.git.BranchSpec>
                <name>{}</name>
            </hudson.plugins.git.BranchSpec>
        </branches>
        <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
        <submoduleCfg class="list"/>
        <extensions/>
    </scm>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <goals>clean package</goals>
    <aggregatorStyleBuild>true</aggregatorStyleBuild>
    <incrementalBuild>false</incrementalBuild>
    <ignoreUpstremChanges>true</ignoreUpstremChanges>
    <ignoreUnsuccessfulUpstreams>false</ignoreUnsuccessfulUpstreams>
    <archivingDisabled>false</archivingDisabled>
    <siteArchivingDisabled>false</siteArchivingDisabled>
    <fingerprintingDisabled>false</fingerprintingDisabled>
    <resolveDependencies>false</resolveDependencies>
    <processPlugins>false</processPlugins>
    <mavenValidationLevel>-1</mavenValidationLevel>
    <runHeadless>false</runHeadless>
    <disableTriggerDownstreamProjects>false</disableTriggerDownstreamProjects>
    <blockTriggerWhenBuilding>true</blockTriggerWhenBuilding>
    <settings class="jenkins.mvn.FilePathSettingsProvider">
        <path>/usr/local/maven3/conf/settings.xml</path>
    </settings>
    <globalSettings class="jenkins.mvn.FilePathGlobalSettingsProvider">
        <path>/usr/local/maven3/conf/settings.xml</path>
    </globalSettings>
    <reporters/>
    <publishers/>
    <buildWrappers/>
    <prebuilders/>
    <postbuilders>
        <jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin plugin="publish-over-ssh@1.19.1">
            <delegate>
                <consolePrefix>SSH: </consolePrefix>
                <delegate plugin="publish-over@0.22">
                    <publishers>
                        <jenkins.plugins.publish__over__ssh.BapSshPublisher plugin="publish-over-ssh@1.19.1">
                            <configName>{}</configName>
                            <verbose>false</verbose>
                            <transfers>
                                <jenkins.plugins.publish__over__ssh.BapSshTransfer>
                                    <remoteDirectory>source_code/activity-web</remoteDirectory>
                                    <sourceFiles>{}</sourceFiles>
                                    <excludes></excludes>
                                    <removePrefix></removePrefix>
                                    <remoteDirectorySDF>false</remoteDirectorySDF>
                                    <flatten>false</flatten>
                                    <cleanRemote>false</cleanRemote>
                                    <noDefaultExcludes>false</noDefaultExcludes>
                                    <makeEmptyDirs>false</makeEmptyDirs>
                                    <patternSeparator>[, ]+</patternSeparator>
                                    <execCommand>{}</execCommand>
                                    <execTimeout>120000</execTimeout>
                                    <usePty>false</usePty>
                                    <useAgentForwarding>false</useAgentForwarding>
                                </jenkins.plugins.publish__over__ssh.BapSshTransfer>
                            </transfers>
                            <useWorkspaceInPromotion>false</useWorkspaceInPromotion>
                            <usePromotionTimestamp>false</usePromotionTimestamp>
                        </jenkins.plugins.publish__over__ssh.BapSshPublisher>
                    </publishers>
                    <continueOnError>false</continueOnError>
                    <failOnError>false</failOnError>
                    <alwaysPublishFromMaster>false</alwaysPublishFromMaster>
                    <hostConfigurationAccess class="jenkins.plugins.publish_over_ssh.BapSshPublisherPlugin" reference="../.."/>
                </delegate>
            </delegate>
        </jenkins.plugins.publish__over__ssh.BapSshBuilderPlugin>
    </postbuilders>
    <runPostStepsIfResult>
        <name>SUCCESS</name>
        <ordinal>0</ordinal>
        <color>BLUE</color>
        <completeBuild>true</completeBuild>
    </runPostStepsIfResult>
</maven2-moduleset>
'''.format(self.description, self.url,self.credentialsId, self.BranchSpec, self.configName, self.remoteDirectory, self.sourceFiles, self.execCommand)
        return str(CONFIG_XML)