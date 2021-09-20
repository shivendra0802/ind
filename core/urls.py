from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import views
from accounts.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.index, name="home"),
]
