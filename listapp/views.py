import getpass
from datetime import datetime,timedelta

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from dateutil.relativedelta import relativedelta
from .models import TaskModel

import json
from dateutil import parser



# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        createuser = request.POST['username']
        print(request.POST)
        password = request.POST['password']
        try:
            User.objects.get(username=createuser)
            return render(request,'signup.html',{'error':'すでに登録されているユーザー名です'})
        except:
            user = User.objects.create_user(createuser,'',password)
            return render(request,'signup.html',{'sam':'samdata'})
    return render(request,'signup.html',{'sam':'samdata'})

def loginfunc(request):
    if request.user.username != '':
        return redirect('list')
    if request.method == 'POST':
        createuser = request.POST['username']
        print(request.POST)
        password = request.POST['password']
        print(createuser,password)
        user = authenticate(request,username=createuser,password=password)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html',{'sam':'samdata'})

@login_required
def listfunc(request):
    print(request.user)
    print(request.user.username)
    now = datetime.now() + timedelta(hours=9)
    dtnow = now.strftime('%Y-%m-%d')
    nodo_list = TaskModel.objects.filter(nottodo='on',author=request.user.username).order_by('starttime')
    do_list = TaskModel.objects.filter(nottodo='off',starttime__startswith=dtnow,author=request.user.username).order_by('starttime')
    if request.method == 'POST':
        choice = request.POST['choiceversion']
        print(choice)
        print(choice == '')
        if choice == 'date' or choice == '':
            selectdate=request.POST['selectdate']
            do_list = TaskModel.objects.filter(nottodo='off',starttime__startswith=selectdate,author=request.user.username).order_by('starttime')
        elif choice == 'week':
            print('week')
            selectdate=request.POST['selectdate']
            dateobj = datetime.strptime(selectdate, '%Y-%m-%d').date()
            maxdate=dateobj + relativedelta(weeks=1)
            do_list = TaskModel.objects.filter(nottodo='off',starttime__range=[selectdate, maxdate],author=request.user.username).order_by('starttime')
        elif choice == 'month':
            print('month')
            selectdate=request.POST['selectdate']
            dateobj = datetime.strptime(selectdate, '%Y-%m-%d').date()
            maxdate=dateobj + relativedelta(months=1)
            do_list = TaskModel.objects.filter(nottodo='off',starttime__range=[selectdate, maxdate],author=request.user.username).order_by('starttime')
    """
    page_data = Paginator(do_list, 3)
    p = request.GET.get('p') 
    listpage = page_data.get_page(p) 
    """
    print('dolist',do_list)
    return render(request,'list.html',{'nodo_list':nodo_list,'do_list':do_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def createfunc(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user.username
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        nottodo = request.POST['nottodo']
        object = TaskModel.objects.create(
            title=title,
            content=content,
            author=author,
            starttime=starttime,
            endtime=endtime,
            nottodo=nottodo,
        )
        print('object: ',object)
        object.save()
        return redirect('list')
    return render(request,'create.html')

def updatefunc(request,pk):
    task = TaskModel.objects.get(pk=pk)
    if task.author != request.user.username:
        return redirect('list')
    if request.method == 'POST':
        print('test')
        if request.POST == {}:
            data = json.loads(request.body)
            task.title=data.get('title')
            task.content=data.get('content')
            task.starttime=data.get('starttime')
            task.endtime=data.get('endtime')
            task.nottodo=data.get('nottodo')
            task.progress=data.get('progress')
            task.memo=data.get('memo')
            task.nottodo='off'
            task.save()
        else:
            newtitle = request.POST['title']
            newcontent = request.POST['content']
            starttime = request.POST['starttime']
            endtime = request.POST['endtime']
            nottodo = request.POST['nottodo']
            progress = request.POST['progress']
            memo = request.POST['memo']
            task.title=newtitle
            task.content=newcontent
            task.starttime=starttime
            task.endtime=endtime
            task.nottodo=nottodo
            task.progress=progress
            task.memo=memo
            task.save()
        return redirect('list')
    return render(request,'update.html',{'task':task})

def deletefunc(request,pk):
    task = TaskModel.objects.get(pk=pk)
    if task.author != request.user.username:
        return redirect('list')
    task.delete()
    return redirect('list')