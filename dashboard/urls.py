# from accounts import views
# from accounts.views import RegistrationView, LoginView,LogoutView
from accounts import views
from django.urls.conf import path
from .views import jobpost, jobdetailview,company_info,qualifi
from dashboard import views

urlpatterns = [
    path('', views.jobpost, name="jobpost"),
    path('job-info/', views.jobdetailview, name="jobdetail"),
    path('comp-info/', views.company_info, name="comapny-info"),
    path('quali/', views.qualifi, name="quali"),
]