from django.urls import path
from accounts import views
# 
from accounts.views import RegistrationView, LoginView,LogoutView
# from accounts.views import logout_view

urlpatterns = [
    # path('register', RegistrationView.as_view()),
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')

    # path('login', views.login, name="login"),
]