"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saved', views.saved,name='saved'),
    path('saved_post', views.saved_post,name= 'saved_post'),
    path('remove_post', views.remove_post,name= 'remove_post'),
    path('delete_post', views.delete_post,name= 'delete_post'),
    path('edit_post', views.edit_post,name= 'edit_post'),
    path('flag_post', views.flag_post,name= 'flag_post'),
]