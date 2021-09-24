# from accounts import views
# from accounts.views import RegistrationView, LoginView,LogoutView
from accounts import views
from django.urls.conf import path
from .views import jobpost, jobdetailview,company_info,qualifi, showdata 
from dashboard import views
from .views import ShowView
app_name='dashboard'

urlpatterns = [
    path('', views.jobpost, name="jobpost"),
    path('job-info/', views.jobdetailview, name="jobdetail"),
    path('comp-info/', views.company_info, name="comapny-info"),
    path('quali/', views.qualifi, name="quali"),
    # path('show-job/', ShowView.as_view(), name="showjob"),
    path('show-job/', views.showdata, name="showdata"),
    path('show-job/<str:slug>/', views.showdatas, name="showdatas"),
]