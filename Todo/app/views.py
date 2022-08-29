from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import generics
from . serializer import TaskSerilizer
from .models import Tasks
import requests

class ReadCreate(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerilizer

class GetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerilizer

def index(request):
    domain=get_current_site(request)
    data=requests.get('http://'+str(domain)+'/readcreate')
    return render(request,'index.html',{'list':data.json()})

def addtask(request):
    domain=get_current_site(request)
    url='http://'+str(domain)+'/readcreate'
    data={'task':request.POST['task1']}
    x=requests.post(url,data)
    return redirect(index)

def deletetask(request,id):
    domain=get_current_site(request)
    url='http://'+str(domain)+'/getupdatedelete/'
    requests.delete(url+str(id))
    return redirect(index)

def updatepage(request,id,task):
    domain=get_current_site(request)
    data = requests.get('http://'+str(domain)+'/readcreate')
    return render(request, 'index.html', {'list': data.json(),'item':task,'id':id})

def updatetask(request,id):
    domain=get_current_site(request)
    url = 'http://'+str(domain)+'/getupdatedelete/'
    data={'task':request.POST['task']}
    requests.put(url + str(id),data)
    return redirect(index)
