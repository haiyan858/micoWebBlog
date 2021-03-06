from django.shortcuts import render

# Create your views here.

from .forms import LoginForm,RegistrationFrom,UserProfileForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse


def user_login(request):
    if request.method =='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse('Welcome You.You have been authenticated successfully!')
            else:
                return HttpResponse("Sorry, Your username or password is not right.")
        else:
            return HttpResponse("Invalid Login")

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def register(request):
    if request.method == "POST":
        user_form = RegistrationFrom(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            # 数据并没有保存到数据库，仅生成了一个数据对象
            new_user = user_form.save(commit=False) #1
            new_user.set_password(user_form.cleaned_data['password']) #2
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("Sorry,you can not register.")
    else:
        user_form = RegistrationFrom()
        userprofile_form = UserProfileForm()
        return render(request,"account/register.html",{"form":user_form,"profile":userprofile_form})

