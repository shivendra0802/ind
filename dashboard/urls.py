# from accounts import views
# from accounts.views import RegistrationView, LoginView,LogoutView
from accounts import views
from django.urls.conf import path
from .views import jobpost, jobdetailview,company_info,qualifi, showdata, subscr, uploadpdf, show_pdf, extract,basepage,test,send_mail_to_all,schedule_mail, mail_letter#, get_jobs, subscribe, get_job
from dashboard import views
from .views import ReviewEmailView
from django.conf.urls.static import static
from django.conf import settings
app_name='dashboard'

urlpatterns = [
    path('', views.jobpost, name="jobpost"),
    path('job-info/', views.jobdetailview, name="jobdetail"),
    path('comp-info/', views.company_info, name="comapny-info"),
    path('quali/', views.qualifi, name="quali"),
    # path('show-job/', ShowView.as_view(), name="showjob"),
    path('show-job/', views.showdata, name="showdata"),
    path('show-job/<str:slug>/', views.showdatas, name="showdatas"),
    path('upload/', views.uploadpdf, name="upload"),
    path('show/', views.show_pdf, name="show"),
    path('extract/', views.extract, name="extract"),
    path('base', views.basepage, name="base"),
    # path('review', ReviewEmailView.as_view(), name="review")
    path('reviews/', ReviewEmailView.as_view(), name="reviews"),
    path('test', views.test, name="test"),
    path('sendmail', views.send_mail_to_all, name="sendmail"),
    path('schedule', views.schedule_mail, name="schedule"),
    # path('getjob', views.get_jobs, name="getjobs"),
    # path('jobs/<int:id>', get_job, name="job_view"),
    path('subscribe', views.subscr, name="subscribe"),
    path('mailletter', views.mail_letter, name="mailletter"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)