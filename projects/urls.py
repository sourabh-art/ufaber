from django.urls import path,include,re_path
from django.conf.urls import url
from . views import *
from . import views


app_name="home"

urlpatterns = [
    path("", views.home, name="home"),
    path("projectadd", views.addproject, name="addproject"),
    path("projectadded", views.projectadded, name="projectadded"),
    path("projectapi", views.rest_api_project, name="projectapi"),
    path("taskapi", views.rest_api_task, name="taskapi"),
    url(r'^project/(?P<project_id>[a-zA-Z0-9 \'&-\_]+)', views.project, name='project'),
    url(r'^projectedit/(?P<project_id>[a-zA-Z0-9 \'&-\_]+)', views.projectedit, name='projectedit'),
    url(r'^project-(?P<project_id>[a-zA-Z0-9 \'&-\_]+)/task/(?P<task_id>[a-zA-Z0-9 \'&-\_]+)', views.task, name='task'),
    path("taskadd", views.taskadd, name="taskadd"),
    url(r'^taskedit/(?P<task_id>[a-zA-Z0-9 \'&-\_]+)', views.taskedit, name='taskedit'),
]
