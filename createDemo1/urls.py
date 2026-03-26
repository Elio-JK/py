"""
URL configuration for createDemo1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from app1 import views

urlpatterns = [   
    path('admin/', admin.site.urls),

    # 访问管理页面 xxx/demo1/路径   ->  访问 views 内的 index 函数 
    path('demo1/', views.index),

    path('app1/', views.page1),

    path('news/', views.news),

    # login 
    path('login/', views.login),


    # orm 操作
    path('orm/', views.orm),

    # student
    path('student/', views.student),

    # users
    path('users/', views.users),
    path('users/<int:id>/detail/', views.user_detail),

    # 模版集成
    path('template/', views.template),
]
