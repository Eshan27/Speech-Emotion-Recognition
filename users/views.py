from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.urls import reverse

from .forms import UserRegisterForm
# Create your views here.
def register(request):
       if request.method == 'POST':
              form = UserRegisterForm(request.POST)
              if form.is_valid():
                     form.save()
                     username = form.cleaned_data.get('username')
                     messages.success(request, f'Account created for {username}!')
                     return redirect('home-page')
       else:
              form = UserRegisterForm
       return render(request,'users/register.html',{'form':form} )
def user_login(request):
    context={}
    if request.method== "POST":
        username=request.POST['username']
        password= request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            messages.success(request, f"You are now logged in as {username}")
            return HttpResponseRedirect(reverse('home-page'))
        else:
            context["Error"] = "Provide valid credentials !!"
            return render(request,"users/login.html",context)
    else:
        return render(request,"users/login.html",context);