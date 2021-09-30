from django.contrib import admin
from .models import JobPost, JobDetails, Qualification, CompanyInformation, Resumeupload, Subscriber, Subscription, MailMessage


# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobDetails)
admin.site.register(Qualification)
admin.site.register(CompanyInformation)
admin.site.register(Resumeupload)
admin.site.register(Subscriber)
admin.site.register(MailMessage)

# admin.site.register(Subscription)
