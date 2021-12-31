from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import Aphorism, UserInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import service

@login_required
def index(request):
  aphorisms = Aphorism.objects.all()
  context = {'aphorisms': aphorisms}
  return render(request, 'index.html', context)

# @login_required
def new(request):
  return render(request, 'new.html')

@login_required
def userinfo(request):
  user = UserInfo.objects.filter(user=request.user)
  info = None
  if (user):
    info = user.values()[0]
  context = {'user': info, 'username': request.user.username}
  print(context)
  return render(request, 'user_info.html', context)

# @login_required
def create(request):
  aphorism = request.POST['aphorism']
  service.create_aphorism(aphorism)
  return redirect('index')

@login_required
def addinfo(request):
  address = mark_safe(request.POST['address'])
  print(type(address))
  sec_number = request.POST['sec_number']
  instance = UserInfo(user=request.user, address=address, sec_number=sec_number)
  instance.save()
  return redirect('userinfo')

def register(request):
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  User.objects.create_user(username, email, password)
  return redirect('index')
