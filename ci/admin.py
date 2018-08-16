from django.contrib import admin

# Register your models here.
from ci.jenkins.jenkins_model import jenkins_info
admin.register(jenkins_info)