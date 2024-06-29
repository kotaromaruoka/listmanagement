import getpass

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import TaskModel



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
    nodo_list = TaskModel.objects.filter(nottodo='on').order_by('starttime')
    do_list = TaskModel.objects.filter(nottodo='off').order_by('starttime')
    if request.method == 'POST':
        selectdate=request.POST['selectdate']
        do_list = TaskModel.objects.filter(nottodo='off',starttime__startswith=selectdate).order_by('starttime')
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
    print('task: ',task)
    if request.method == 'POST':
        newtitle = request.POST['title']
        newcontent = request.POST['content']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        nottodo = request.POST['nottodo']
        task.title=newtitle
        task.content=newcontent
        task.starttime=starttime
        task.endtime=endtime
        task.nottodo=nottodo
        task.save()
        return redirect('list')
    return render(request,'update.html',{'task':task})

def deletefunc(request,pk): 
    task = TaskModel.objects.get(pk=pk)
    task.delete()
    return redirect('list')
    