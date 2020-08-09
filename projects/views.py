from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Projects,Task
import os
from rest_framework.response import Response
from django.conf import settings
from .serialzers import ProjectSerializer,TaskSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
import json
from django.core.files.storage import FileSystemStorage

@api_view(["GET"])
def rest_api_project(request):
    all_project=Projects.objects.all()
    serializer=ProjectSerializer(all_project,many=True)
    return Response(serializer.data)
@api_view(["GET"])
def rest_api_task(request):
    all_task=Task.objects.all()
    serializer=TaskSerializer(all_task,many=True)
    return Response(serializer.data)

def home(request):
    SERVER=request.META["HTTP_HOST"]
    if SERVER=="127.0.0.1:8000":
        url="http://127.0.0.1:8000/projectapi"
    else:
        url="https://ufabertest.herokuapp.com/projectapi"
    r=requests.get(url)
    parm=r.json()
    
    return render(request,'home.html',{"parm":parm})
def addproject(request):
    return render(request,"addproject.html")

def projectadded(request):
    name=request.POST.get("name")
    description=request.POST.get("description")
    start_dat=request.POST.get("stdt")
    end_date=request.POST.get("enddt")
    duration=request.POST.get("days")
    print(duration,"durationdurationdurationduration")
    duration=int(duration)
    photo=request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    print(filename,"filenamefilenamefilenamefilenamefilename")
    uploaded_file_url = fs.url(filename)
    print(uploaded_file_url,"uploaded_file_urluploaded_file_urluploaded_file_urluploaded_file_url")
    Projects.objects.create(name=name,description=description,startdate=start_dat,enddate=end_date, photo=photo,duration=duration)
    return redirect("home:home")
def project(request,project_id):
    SERVER=request.META["HTTP_HOST"]
    if SERVER=="127.0.0.1:8000":
        url="http://127.0.0.1:8000/projectapi"
        url2="http://127.0.0.1:8000/taskapi"
    else:
        url="https://ufabertest.herokuapp.com/projectapi"
        url2="https://ufabertest.herokuapp.com/taskapi"
    r=requests.get(url)
    parm=r.json()

    
    r2=requests.get(url2)
    r2=r2.json()
    print(parm,"mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    project={}
    print(project_id)
    if len(parm) == 1:
        project=r.json()[0]
  
    else:    
        for i in parm:
            if i['id']==int(project_id):
                project["id"]=i['id']
                project["name"]=i['name']
                project["description"]=i['description']
                project["startdate"]=i['startdate']
                project["enddate"]=i['enddate']
                project["photo"]=i['photo']
                project["duration"]=i['duration']
    print(project,"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

    task=[]
    # print(r2,"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
    project_id=int(project_id)
   

    if len(r2) == 1:
        task=r2
    elif len(r2) == 1:
        task=[]
    else:
         
        for j in r2:
            if j['project']==project_id:
                task.append(dict(id=j["id"],name=j["name"],description=j["description"],startdate=j["startdate"],enddate=j["enddate"],asign_to=j["asign_to"],project=j["project"]))
                # task.append(dict(name=j["name"]))
                # task.append(dict(id=j["project"]))
                # task.append(dict(id=j["startdate"]))
                # task.append(dict(id=j["enddate"]))
                # task[j["id"]]["id"]=j["id"]
                # task[j["id"]]["project"]=j["project"]
                # task[j["id"]]["description"]=j["description"]
                # task[j["id"]]["startdate"]=j["startdate"]
                # task[j["id"]]["enddate"]=j["enddate"]
                # task[j["id"]]["asign_to"]=j["asign_to"]
                
    
    parm={"project":project,"task":task}
    print(task,"cccccccccccccccccccccccccccc")
    return render(request,"project.html",parm)
def projectedit(request,project_id):
    name=request.POST.get("name")
    description=request.POST.get("description")
    start_dat=request.POST.get("stdt")
    end_date=request.POST.get("enddt")
    duration=request.POST.get("days")
    print(duration,"durationdurationdurationduration")
    duration=int(duration)
    photo=request.FILES['photo']

    # fs = FileSystemStorage()
    # filename = fs.save(photo.name, photo)
    # print(filename,"filenamefilenamefilenamefilenamefilename")
    # uploaded_file_url = fs.url(filename)
    Projects.objects.filter(id=project_id).update(name=name,description=description,startdate=start_dat,enddate=end_date, photo=photo,duration=duration)

    return redirect("home:home")
def taskadd(request):
    name=request.POST.get("name")
    description=request.POST.get("description")
    start_dat=request.POST.get("stdt")
    end_date=request.POST.get("enddt")
    duration=request.POST.get("days")
    asign_to=request.POST.get("assign")
    project_id=request.POST.get("project")
    project_id=int(project_id)
    print(project_id)
    project_name=request.POST.get("project_name")
    
    Task.objects.create(name=name,description=description,startdate=start_dat,enddate=end_date,project=project_id,project_name=project_name, asign_to=asign_to,duration=duration)
    return redirect("home:project", project_id=project_id)
def task(request,project_id,task_id):
    SERVER=request.META["HTTP_HOST"]
    if SERVER=="127.0.0.1:8000":
        url2="http://127.0.0.1:8000/taskapi"
    else:
        url2="https://ufabertest.herokuapp.com/taskapi"
    r2=requests.get(url2)
    parm=r2.json()
    my_task={}
    print("hhhhhhhhhhhhhhhhhhh")
    if len(parm) == 1:
        my_task=r2.json()[0]
    else:    
        for i in parm:
            print(i['id']==int(task_id))
            if i['id']==int(task_id):
                my_task["id"]=i['id']
                my_task["name"]=i['name']
                my_task["description"]=i['description']
                my_task["startdate"]=i['startdate']
                my_task["enddate"]=i['enddate']
                my_task["duration"]=i['duration']
                my_task["project"]=i['project']

    return render(request,"task.html",{"task":my_task})
def taskedit(request,task_id):
    name=request.POST.get("name")
    description=request.POST.get("description")
    start_dat=request.POST.get("stdt")
    end_date=request.POST.get("enddt")
    duration=request.POST.get("days")
    asign_to=request.POST.get("assign")
    project_id=request.POST.get("project")
   
    project_id=int(project_id)

    Task.objects.update(name=name,description=description,startdate=start_dat,enddate=end_date, asign_to=asign_to,duration=duration)
    return redirect("home:project",project_id=project_id)   