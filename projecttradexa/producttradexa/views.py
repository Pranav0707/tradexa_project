from django.shortcuts import redirect, render

from usertradexa.decorators import unauthenticated
from .form import *
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def productview(request):
    form=ProductForm()
    if request.method=='POST':
            form=ProductForm(request.POST)
    if form.is_valid():
            user=form.save()
            return redirect('postview')

    context={'form':form}
    return render(request,'producttradexa/product.html',context)