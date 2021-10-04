from django.db import models
from django.db.models import fields
from dashboard.models import JobDetails, JobPost, Qualification, Resumeupload, CompanyInformation, Subscriber,MailMessage
from django.forms import ModelForm
# from dashboard.models import JobPost
from django import forms







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

class DocumentForm(ModelForm):
    class Meta:
        model = Resumeupload
        fields = '__all__'

class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]

from django import forms

# class SubscribersForm(forms.Form):
#     email = forms.EmailField(label='Your email',
#                              max_length=100,
#                              widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'

# from dashboard.tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    review = forms.CharField(
        label="Review", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])        