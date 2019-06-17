"""FristDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.shortcuts import render,redirect # redirect()重定向模块 render获取html文件内容


def login(request):
    if request.method == "GET":
        return render(request,'1.html')
    else:
        # 请求得到用户输入的数据
        data1 = request.POST.get('username')
        data2 = request.POST.get('password')
        if data1 == 'root' and data2 == 'password':
            # 重定向到百度界面,表示成功
            return redirect('http;//www.baidu.com')



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login),
]
