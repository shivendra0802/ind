from django.db import models
from django.db.models import fields
from .models import JobPost, JobDetails, Qualification, CompanyInformation
from django.forms import ModelForm


class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'


class JobDetailsForm(ModelForm):
    class Meta:
        model = JobDetails
        fields = '__all__'


class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'

class CompanyInformationForm(ModelForm):
    class Meta:
        model = CompanyInformation
        fields = '__all__'