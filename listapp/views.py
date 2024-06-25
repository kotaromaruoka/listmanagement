from django.shortcuts import render
from django.contrib.auth.models import User


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