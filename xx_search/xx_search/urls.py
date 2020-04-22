"""xx_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    # path中的第一个参数，为url路径，并不是应用名称。为空''则是首页。

    path('api/admin/', admin.site.urls),
    path('api/search/', views.index, name="index"),
    path('api/login/', views.login, name="login"),
    path('loginstatus/',csrf_exempt(views.loginstatus),name='loginstatus'),
    path('login_out/', views.logout_view, name="login_out"),
    path('api/mark/', include('marks.urls')),
    path('api/blog/',include('blog.urls')),
    path('api/do_something/',views.do_something,name='do_something')
]
