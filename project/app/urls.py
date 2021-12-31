from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('create', views.create, name='create'),
    path('new', views.new, name='new'),
    path('userinfo', views.userinfo, name='userinfo'),
    path('addinfo', views.addinfo, name='addinfo'),
]