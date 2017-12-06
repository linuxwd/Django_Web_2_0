"""Django_Web_2_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views
# 执行autodiscover函数，该函数是根据settings.INSTALLED_APPS来逐个处理每个模块的，
# 注册了模块却无法生效，肯定是因为没有将模块添加到配置文件的INSTALLED_APPS中。
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^here/$', views.here),
    re_path(r'^(\d{1,2})/plus/(\d{1,2})',views.add),
    re_path(r'^(\d{1,2})/math/(\d{1,2})', views.math),
]
