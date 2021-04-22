from typing import Set, Any

from django.shortcuts import render
from playsound import playsound
import speech_recognition as sr

from .models import Songs
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages, auth
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import datetime
from process import livePredictions
def hi(request):    
    all_files = Songs.objects.all()
    
    return render(request,'LoginApp/hi.html',{'titles' : all_files})

def about(request):
    return render(request,'LoginApp/about.html' ,{'title': 'About'})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "Logged out successfully!")
        return render(request,"LoginApp/login.html",{});
    return render(request, "LoginApp/hi.html", {});
name = ""
f_type = ""
def record(request):
    global name
    global f_type
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name,uploaded_file)
    f_type = fs.save(uploaded_file.content_type,uploaded_file)
    print(name)
    return render(request,"LoginApp/record.html")
def products(request):
    obj=data.objects.all()
    context={
        'objects':obj
    }
    return render(request,'LoginApp/products.html',context)

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        global name
        global f_type
        name = fs.save(uploaded_file.name,uploaded_file)
        f_type = fs.save(uploaded_file.content_type,uploaded_file)
        context['url'] = fs.url(name)
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file.content_type)
        #playsound(name)
        now=datetime.datetime.now()
        date1 = now.strftime("%Y-%m-%d")
        print(date1)
        time1 = now.strftime("%H:%M:%S")
        print(time1)
        song = Songs(file_type=uploaded_file.content_type,song_title=name,date=date1,time=time1)
        song.save()


        # r = sr.Recognizer()
        # with sr.AudioFile(uploaded_file)as source:
        #     audio = r.listen(source)
        #     try:
        #         text = r.recognize_google(audio)
        #         print('Working On........')
        #         print(text)
        #     except:
        #         print('sorry run again')
    return render(request, 'LoginApp/upload.html', context)

def prediction(request,id):
    pred = livePredictions(path='./testing10_model.h5', file=id)
    pred.load_model()
    pred.makepredictions()
    return render(request, 'LoginApp/prediction.html',{'f_name':id})