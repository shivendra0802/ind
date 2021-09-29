from core.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import urls, views
from accounts.views import  index
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', views.index, name="home"),
] 


