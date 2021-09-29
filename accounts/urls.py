from django.urls import path
from accounts import views
from django.conf.urls import include, __path__
from accounts import views
from accounts.views import RegistrationView, LoginView,LogoutView, contact, about, new
# from accounts.views import logout_view

urlpatterns = [
    # path('register', RegistrationView.as_view()),
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('new', views.new, name="new"),
]