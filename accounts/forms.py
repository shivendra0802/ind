from django import forms
from django.forms import fields
from .models import CustomUser
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .models import Employer

class EmpRegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = Employer
        fields = ['email','password1', 'password2']










# class JobseekerSignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)
#     location = forms.CharField(required=True)

#     class Meta:
#         model = CustomUser

#     def save(self):
#         user = super().save(commit=False)
#         user.is_jobseeker = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         jobseeker = Jobseeker.objects.create(user=user)
#         jobseeker.phone_number=self.cleaned_data.get('phone_number')
#         jobseeker.location=self.cleaned_data.get('location')
#         jobseeker.save()
#         return user

# class EmployerSignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)
#     designation = forms.CharField(required=True)

#     class Meta:
#         model = CustomUser

#     # @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         # user.is_jobseeker = True
#         user.is_employer = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         employer = Employer.objects.create(user=user)
#         employer.phone_number=self.cleaned_data.get('phone_number')
#         employer.designation=self.cleaned_data.get('designation')
#         employer.save()
#         return user