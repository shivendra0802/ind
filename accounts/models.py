from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from accounts.managers import CustomManager
# from multiselectfield import MultiSelectField





class User(models.Model):
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)



class Jobseeker(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)    

# Create your models here.

# class UserType(models,Model):
#     CHOICES = [
#         ('employer', 'employer'),
#         ('jobseeker', 'jobseeker')
#     ]
#     # is_employer = models.BooleanField(default=False)
#     # is_jobseeker = models.BooleanField(default=True)
#     type = models.CharField(choices=CHOICES, max_length=100)

#     def __str__(self):
#         return self.type



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # auth_provider = models.CharField(
    #     max_length=255, blank=False,
    #     null=False, default=AUTH_PROVIDERS.get('email'))



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()
    

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



















































    
    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
    #     }



# def unique_rand():
#     '''
#     For generating unique_id in user profile
#     '''
#     while True:
#         code = CustomUser.objects.make_random_password(length=8)
#         if not Profile.objects.filter(unique_id=code).exists():
#             return code




# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)