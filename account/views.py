from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm,PasswordResetForm1,UpdatePassword
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import  messages           
# Create your views here.

def registration(request):
    if request.user.is_authenticated:
        return redirect('article_list')
    if request.method=='GET':
        form=RegistrationForm()
        context={
            "form": form
    }
        return render(request, "registration/signup.html",context)
        
    data=request.POST
    print(data)
    form=RegistrationForm(data)
    if form.is_valid():
        form.save()
        messages.success(request, "Account muvaffaqiyatli yaratildi!  ")
        return redirect('login')
    context={
            "form": form
    }
    return render(request, "registration/signup.html",context)
        
def login_user(request):
    if request.user.is_authenticated:
        return redirect('article_list')
        
    if request.method=='GET':
        form=LoginForm()
        context={
            "form": form
                }
        return render(request, "registration/login.html",context)
    
    data=request.POST
    form=LoginForm(data=data)
    
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        print(username, password)
        user=authenticate(request, username=username,password=password) 
        print(user)
        if user is not None:
            messages.success(request, "Tizimga  muvaffaqiyatli yaratildi!  ")
            login(request, user)
            return redirect('article_list')
    context={
    "form": form
        }
    return render(request,'registration/login.html',context)
    
    
def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('article_list')
        
    logout(request)
    messages.info(request, "Tizimdan chiqildi!  ")
    
    return redirect('article_list')

import random
def create_password():
    sign=['1','2','3','4','5','6','7','8','9','0']
    new_p=random.choices(sign, k=5) 
    return str(new_p)

def password_reset(request):
    if request.method=='GET':
        form=PasswordResetForm1()
        context={
            "form": form
                }
        return render(request, "registration/password_reset.html",context)


    data=request.POST
    form=PasswordResetForm1(data=data)
    
    if form.is_valid():
        username=form.cleaned_data.get('username')
        user=User.objects.get(username=username)
        new_p=create_password()
        user.set_password(str(new_p))
        user.save()
        messages.warning(request, "Parolingz o'zgartirildi, yangi parol yuborildi!  ")
        
        print(f"Email: {user.email}")
        print(f"Password: {new_p}")
        
        
        return redirect('login')
    context={
        "form": form
            }
    return render(request, "registration/password_reset.html",context)



def update_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method=='GET':
        form=UpdatePassword()
        context={
            "form": form
                }
        return render(request, "registration/update_password.html",context)
    
    user=request.user
    data=request.POST
 
    form=UpdatePassword(data=data)
    
    if form.is_valid():
        password=form.cleaned_data.get("new_password")
        old_password=form.cleaned_data.get("old_password")
        is_user=authenticate(request, username=user.username,password=old_password) 
        print(is_user)
        
        
        if is_user is not None:
            user.set_password(password)
            user.save()   
            login(request,user)
            messages.success(request, "Parol yangilandi!  ")
            
            return redirect('article_list')
        
        else:
            print(" old_password xato kiritildi!")
            messages.error(request, "old_password xato kiritildi! ")
            
            context={
                    "form": form
                        }
            return render(request, "registration/update_password.html",context)
        
    messages.error(request,  form.errors)

    context={
            "form": form
                }
    return render(request, "registration/update_password.html",context)
