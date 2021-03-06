"""django_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ci import views
from ci.jenkins import jenkins_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.test),
    path('get_all_jobs_info', jenkins_views.get_all_jobs_info),
    path('get_jobs_list', jenkins_views.get_jobs_list),
    path('get_job_config', jenkins_views.get_job_config),
    path('build_job_by_params', jenkins_views.build_job_by_params),
    path('get_last_build', jenkins_views.get_last_build),
    path('create_job', jenkins_views.create_job)
]
