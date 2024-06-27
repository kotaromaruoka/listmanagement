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
    object_list = TaskModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def createfunc(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user.username
        object = TaskModel.objects.create(
            title=title,
            content=content,
            author=author,
        )
        print('object: ',object)
        object.save()
        render(request,'create.html')
    return render(request,'create.html')

def updatefunc(request,pk):
    task = TaskModel.objects.get(pk=pk)
    print('task: ',task)
    if request.method == 'POST':
        newtitle = request.POST['title']
        newcontent = request.POST['content']
        task.title=newtitle
        task.content=newcontent
        task.save()
        return redirect('list')
    return render(request,'update.html',{'task':task})

def deletefunc(request,pk): 
    task = TaskModel.objects.get(pk=pk)
    task.delete()
    return redirect('list')
    