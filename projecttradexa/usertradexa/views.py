from django.shortcuts import redirect, render

from producttradexa.models import Product
from usertradexa.models import Post
from .form import PostForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@unauthenticated
def userRegistration(request):
    form=RegisterForm()
    if request.method=='POST':
            form=RegisterForm(request.POST)
    if form.is_valid():
            user=form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'usertradexa/registeration.html',context)

@unauthenticated
def UserLogin(request):
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('userpost')
            else:
                messages.info(request,'Username Or Password Is Incorrect!!')
                

        context={}
        return render(request,'usertradexa/login.html',context)

def UserLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')

def userPost(request):

    form=PostForm()
    if request.method=='POST':
            form=PostForm(request.POST)
    if form.is_valid():
            user=form.save()
            return redirect('product')
    context={'form':form}
    return render(request,'usertradexa/userpost.html',context)

@login_required(login_url='login')
def postview(request):
        post=Post.objects.all()
        product=Product.objects.all()
        context={'post':post,'product':product}
        return render(request,'usertradexa/postview.html',context)
