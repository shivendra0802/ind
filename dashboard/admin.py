from django.contrib import admin
from .models import JobPost, JobDetails, Qualification, CompanyInformation, Resumeupload


# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobDetails)
admin.site.register(Qualification)
admin.site.register(CompanyInformation)
admin.site.register(Resumeupload)
