import json
import uuid
import datetime
import requests
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone
from datetime import *
import numpy as np
from django.shortcuts import render, HttpResponse,redirect
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pickle
import streamlit as st
import pandas as pd
from datetime import datetime
from django.contrib.auth.models import User
from mysite.models import Contact,Location
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pickle
import pandas as pd
import sklearn
import joblib



#Create your views here.

#api_key = 'YOUR_API_KEY';

#api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key

#api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=b461135c657f4cb8913ef6b7c85db7b3'



"""def get_ip_geolocation_data(ip_addr):
    print(ip_addr)
    #response = requests.get(api_url + "&ip_address=" + ip_addr)
    response = requests.get(api_url)
    return response.content
    print(response.content)


def index(request):
    def get_client_ip_address(request):
        req_headers = request.META
        x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for_value:
            ip_addr = x_forwarded_for_value.split(',')[-1].strip()
        else:
            ip_addr = req_headers.get('REMOTE_ADDR')
        return ip_addr

    ip_addr = get_client_ip_address(request)
    geolocation_json = get_ip_geolocation_data(ip_addr)
    geolocation_data = json.loads(geolocation_json)
    print(geolocation_data)
    country = geolocation_data['country']
    region = geolocation_data['region']
    u = Location(person=ip_addr, country=country, region=region)
    u.save()
    print(ip_addr)
    result = Location.objects.filter(Q(person__icontains=ip_addr))
    if len(result)==1:
        print("User Exist")
    elif len(result)>1:
        print("Other Users are Also Available")
    else:
        u.save()
        print("User is Unique")
    count = Location.objects.all().count()
    print("Total User is",count)
    return render(request, 'index.html')"""


def index(request):
    return render(request, 'index.html')

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Thanks for Contacting Us')
    return render(request, 'contact.html')


def signup(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/login')
    return render(request, 'signup.html')


def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')

def user_list(request):
    all_users = User.objects.all()
    # Now you can use "all_users" in your template or perform further operations on it.
    return render(request, 'user_list.html', {'users': all_users})



def dashboard(request):
    return render(request, 'afterlogin.html')

def dashboard_inner(request):
    return render(request, 'afterlogin-categotries.html')

def main_dashboard(request):
    return render(request, 'main_dashboard.html')



