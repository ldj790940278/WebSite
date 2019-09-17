"""WebSite URL Configuration

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
from django.conf import \
    settings
from django.conf.urls import \
    url
from django.conf.urls.static import \
    static
from django.contrib import admin
from django.template.context_processors import request
from django.urls import \
    path, \
    re_path, \
    include
from django.shortcuts import HttpResponse,render,redirect
from django.shortcuts import HttpResponse
from FirstWeb import views;

from django.urls import path, re_path

from materials.models import \
    Fabric


def login(request):
    print(request.method)

    # return HttpResponse('昨天晚上在狂风暴雨中，我和拓拓小美女渡过了一个狂乱的夜晚')
    if request.method=="GET":
        return render(request,
                  '2login.html')
    else:
        e=request.POST.get("email")
        p=request.POST.get("pwd")
        if e=="root" and p=="123":
            return redirect("http://www.baidu.com")
        else:
            return render(request,
                      '2login.html',
                          {'msg1':['用户名错误','密码错误'],
                           'msg2':{'k1':['k1的value1','k1的v2'],'k2':'value3'},
                           'msg3':['1','2','3']
                           }

                          )
def boot(request):
    return render(request,
                  'boot.html')


def grid(request):
    return render(request,
                  'GridSample.html')

def Main(request):

    # return render(request,
    #               'Test/0Main.html')
    return render(request,
                  'center.html')

urlpatterns = [
    path('',Main),
    path('admin/', admin.site.urls),
    path('login/', login),
    path('boot/',boot),
    path('grid/',grid),
    # url(r'^upload/', upload),
    path('cla/',views.cla),
    path('newClass/',views.newStudent),
    path('materials/',include('materials.urls')),
    path('music/',include('music.urls')),
    path('myblog/',include('myblog.urls')),
    # path('newStudent/',views.newStudent),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)