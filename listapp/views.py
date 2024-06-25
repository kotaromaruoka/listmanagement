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