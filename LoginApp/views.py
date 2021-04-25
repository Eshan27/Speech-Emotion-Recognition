from typing import Set, Any

from django.shortcuts import render
from playsound import playsound
import speech_recognition as sr
import random
import string
import pyaudio
import wave
from .models import Songs
from .models import record
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages, auth
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import datetime
from LoginApp.process import livePredictions
import warnings
import os
def hi(request):    
    all_files = Songs.objects.all()
    
    return render(request,'LoginApp/hi.html',{'titles' : all_files})

def about(request):
    return render(request,'LoginApp/about.html' ,{'title': 'About'})
def home(request):
    return render(request,'LoginApp/HomePage.html',{'title': 'About'})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "Logged out successfully!")
        return render(request,"LoginApp/login.html",{});
    return render(request, "LoginApp/hi.html", {});
name = ""
f_type = ""
def record(request):
    # global name
    # global f_type
    # fs = FileSystemStorage()
    # name = fs.save(uploaded_file.name,uploaded_file)
    # f_type = fs.save(uploaded_file.content_type,uploaded_file)
    # print(name)
    # warnings.filterwarnings('ignore')    
    # def record_my_audio():
    #     time_duration = 10
    #     FORMAT = pyaudio.paInt16
    #     CHANNELS = 2
    #     RATE = 44100
    #     CHUNK = 1024
    #     RECORD_SECONDS = time_duration
    #     print("Recording...")

    #     audio = pyaudio.PyAudio()

    #     # start Recording
    #     stream = audio.open(format=FORMAT, channels=CHANNELS,
    #                         rate=RATE, input=True,
    #                         frames_per_buffer=CHUNK)
    #     frames = []

    #     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #         data = stream.read(CHUNK)
    #         frames.append(data)

    #     stream.stop_stream()
    #     stream.close()
    #     audio.terminate()
    #     print("Finished Recording\n")
    #     return_data = [frames, stream, audio]
    #     return return_data

    # def save_my_recording(destination_filename, stream, frames, audio):
    #     channels = stream._channels
    #     rate = stream._rate
    #     format = stream._format

    #     wave_File = wave.open(destination_filename, 'wb')
    #     wave_File.setnchannels(channels)
    #     wave_File.setsampwidth(audio.get_sample_size(format))
    #     wave_File.setframerate(rate)
    #     wave_File.writeframes(b''.join(frames))
    #     wave_File.close()
    
    # def play_sound(path_to_file):

    #     print("Now Playing.....")
    #     chunk = 1024
    #     f = wave.open(path_to_file)
    #     p = pyaudio.PyAudio()

    #     stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
    #                     channels=f.getnchannels(),
    #                     rate=f.getframerate(),
    #                     output=True)        
    #     data = f.readframes(chunk)

    #     for i in range(len(data)):
    #         stream.write(data)
    #         data = f.readframes(chunk)

    #     stream.stop_stream()
    #     stream.close()

    #     p.terminate()

    # data = record_my_audio()
    # f_name1 = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    # file_name = './media/'+f_name1+'.wav'
    # save_my_recording(file_name, data[1], data[0], data[2])    
    # playsound(file_name)
    # print(f_name1)
    # now=datetime.datetime.now()
    # d1 = now.strftime("%Y-%m-%d")
    # t1 = now.strftime("%H:%M:%S")
    # f_typ = "recorded"
    # f_name2 = f_name1+".wav"
    # # r_f = record(s_title=f_typ,d=d1,t=t1)
    # # r_f.save()
    # song = Songs(file_type=f_typ,song_title=f_name2,date=d1,time=t1)
    # song.save()
    # # file_name1 = './recorded/'+f_name+'.wav'
    # for item in os.scandir(file_name1):
    #     print(item.name, item.path, item.stat().st_size, item.stat().st_atime)
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
    return render(request, 'LoginApp/upload.html', context)

def prediction(request,id):
    pred = livePredictions(path='LoginApp/SER_model.h5', file='media/'+id)
    pred.load_model()
    pre1 = pred.makepredictions()
    print(pre1)
    
    return render(request, 'LoginApp/prediction.html',{'f_name':pre1})

def record_audio(request):
    # global name
    # global f_type
    # fs = FileSystemStorage()
    # name = fs.save(uploaded_file.name,uploaded_file)
    # f_type = fs.save(uploaded_file.content_type,uploaded_file)
    # print(name)
    warnings.filterwarnings('ignore')    
    # if request.GET('sort-btn'):
    
    def record_my_audio():
        time_duration = 10
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = time_duration
        print("Recording...")

        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("Finished Recording\n")
        return_data = [frames, stream, audio]
        return return_data

    def save_my_recording(destination_filename, stream, frames, audio):
        channels = stream._channels
        rate = stream._rate
        format = stream._format

        wave_File = wave.open(destination_filename, 'wb')
        wave_File.setnchannels(channels)
        wave_File.setsampwidth(audio.get_sample_size(format))
        wave_File.setframerate(rate)
        wave_File.writeframes(b''.join(frames))
        wave_File.close()
    
    def play_sound(path_to_file):

        print("Now Playing.....")
        chunk = 1024
        f = wave.open(path_to_file)
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)        
        data = f.readframes(chunk)

        for i in range(len(data)):
            stream.write(data)
            data = f.readframes(chunk)

        stream.stop_stream()
        stream.close()

        p.terminate()

    data = record_my_audio()
    f_name1 = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    file_name = './media/'+f_name1+'.wav'
    save_my_recording(file_name, data[1], data[0], data[2])    
    playsound(file_name)
    print(f_name1)
    now=datetime.datetime.now()
    d1 = now.strftime("%Y-%m-%d")
    t1 = now.strftime("%H:%M:%S")
    f_typ = "recorded"
    f_name2 = f_name1+".wav"
    # r_f = record(s_title=f_typ,d=d1,t=t1)
    # r_f.save()
    song = Songs(file_type=f_typ,song_title=f_name2,date=d1,time=t1)
    song.save()
    cits = ""+f_name2
    # file_name1 = './recorded/'+f_name+'.wav'
    # for item in os.scandir(file_name1):
    #     print(item.name, item.path, item.stat().st_size, item.stat().st_atime)
    return render(request,"LoginApp/record.html",{'f_name':f_name1,'cits': cits,'some_flag': True})
