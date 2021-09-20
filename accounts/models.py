from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from accounts.managers import CustomManager
# from multiselectfield import MultiSelectField





# class User(models.Model):
#     is_employer = models.BooleanField(default=False)
#     is_jobseeker = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)



# class Jobseeker(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     email = models.EmailField(max_length=200)
#     phone_number = models.CharField(max_length=20)
#     location = models.CharField(max_length=20)

# class Employer(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     email = models.EmailField(max_length=200)
#     phone_number = models.CharField(max_length=20)
#     designation = models.CharField(max_length=20)    

# Create your models here.

# class UserType(models.Model):
CHOICES = [
        ('employer', 'employer'),
        ('jobseeker', 'jobseeker')
]




class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_type_data = (("employer", "employer"), ("jobseeker","jobseeker"))
    role = models.CharField(default="jobseeker",  choices=user_type_data, max_length=255)
    # UserType = models.CharField(max_length=200, choices=CHOICES)
    email = models.EmailField(_('email address'), unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_employer = models.BooleanField(default=False)
    # is_jobseeker = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # class Types(models.TextChoices):
    #     EMPLOYER = "employer", "Employer"
    #     JobSeeker = "JobSeeker", "JOBSEEKER"
    
    # default_type = Types.JobSeeker

    # type = models.CharField(_('Types'), max_length=255, choices=Types.choices, default=default_type)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()
    

    def __str__(self):
        return self.email


class Employer(models.Model):
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']



    def __str__(self):
        return self.email

class Jobseeker(models.Model):
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.email

# MY_CHOICES = (
#         (1, 'Employer'),
#         (2, 'Job Seeker')
#     )

# CHOICES = (('item_key1', 'Item title 1.1'),

# class MyModel(models.Model):
#     my_field = MultiSelectField(choices=MY_CHOICES)
#     my_field2 = MultiSelectField(choices=MY_CHOICES2,
#                                  max_choices=3,
#                                  max_length=3)



















































    





