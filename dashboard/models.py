from django.core.mail import message
from django.db import models

from dashboard.email import send_review_email
from .make_slug import unique_slug_generator,random_string_generator
import string, random
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
# from dashboard.email import send_review_email
# from dashboard.views import schedule_mail
# Create your models here.
# from dashboard.views import schedule_mail
from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from dashboard.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

role = (
    ("Owner", "Owner"),
    ("CEO",    "CEO"),
    ("Recruiter", "Recuriter"),
    ("Talent Acquisition", "Talent Acquisition"),
    ("Assistant or Officer Manager", "Assistant or Officer Manager"),
    ("Hiring Manager", "Hiring Manager"),
    ("Human Resource Generalist", "Human Resource Generalist"),
    ("Other", "Other")
)

category = (
    ("Back End Developer", "Back End Developer"),
    ("Front End Developer", "Front End Developer"),
    ("iOS Developer", "iOS Developer"),
    ("Machine Learning", "Machine Learning")
)

wfh = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("Temporarily due to COVID-19", "Temporarily due to COVID-19"),
)

# from .views import mail_letter

class JobPost(models.Model):
    id = models.BigAutoField(primary_key=True)    
    company_name =                    models.CharField(max_length=255)
    your_role_in_hiring_process =     models.CharField(max_length=255, choices=role)
    job_title =                       models.CharField(max_length=255)
    job_category =                    models.CharField(max_length=255,choices=category)
    location_of_company =             models.CharField(max_length=255)
    street_address =                  models.CharField(max_length=255)
    city =                            models.CharField(max_length=255)
    country =                         models.CharField(max_length=255)
    work_from_home =                  models.CharField(max_length=255, choices=wfh)
    post_language =                   models.CharField(max_length=255)
    no_of_hiring =                    models.PositiveIntegerField()
    always_hiring =                   models.BooleanField()
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.company_name


# @receiver(pre_save, sender=JobPost)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=JobPost)


# def post_save_receiver(sender, instance, *args, **kwargs):
#     instance = mail_letter(instance)

# post_save.connect(post_save_receiver, sender=JobPost)


# @receiver(post_save, sender=JobPost)
# def message_alert(sender, instance, **kwargs, schedule_mail):
    # print('--------------')
    # def schedule_mail(request):
    #     print('++++++++++++')
    #     schedule, created = CrontabSchedule.objects.get_or_create(hour = 0, minute = 5)
    #     print('===========')
    #     task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"1", task='dashboard.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    #     print('**********')
    #     return HttpResponse("Done")
    # instance.schedule_mail  = schedule_mail
    # instance.product.stock -= instance.amount
    # instance.product.save()

class CompanyInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    comp_id = models.ForeignKey(JobPost, on_delete=models.CASCADE, null=True,default=1)
    your_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    # company_name = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    phone_no = models.PositiveIntegerField()
    company_size = models.IntegerField()
    where_here_about_us = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

emp_type = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)
contr_tye = (
    ("Temprory", "Temprory"),
    ("Contract", "Contract"),
    ("Fresher", "Fresher"),
    ("Internship", "Internship"),
)
schedule = (
    ("Morning Shift", "Morning Shift"),
    ("Night Shift", "Night shift"),
)

s_pay = (
    ("Commission pay", "Commission pay"),
    ("Overtime pay", "Overtime pay"),
    ("Shift allowance", "Shift allowance"),
    ("Joining bonus", "Joining bonus")
)

ben = (
    ("Cell phone reimbursement", "Cell phone reimbursement"),
    ("Commuter assistance", "Commuter assistance"),
    ("Flexible schedule", "Flexible schedule")
)

class JobDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    jobd_id = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=255, choices=emp_type)
    contract_type = models.CharField(max_length=255, choices=contr_tye)
    job_schedule = models.CharField(max_length=255, choices=schedule)
    # start_date = models.DateField()
    supplement_pay = models.CharField(max_length=255, choices=s_pay)
    benefits = models.CharField(max_length=255, choices=ben)
    # want_to_submit_resume = models.BooleanField(max_length=255)
    # deadline = models.BooleanField(max_length=255)
    job_description = models.TextField()

    def __str__(self):
        return self.employment_type    

quali = (
    ("Secondary(10th Pass)", "Secondary(10th Pass)"),
    ("Higher Secondary(12th Pass)", "Higher Secondary(12th Pass)"),
    ("Diploma", "Diploma"),
    ("Bachelor's", "Bachelor's"),
    ("Master's", "Master's"),
    ("Doctorate", "Doctorate")
)


class Qualification(models.Model):
    id = models.BigAutoField(primary_key=True)
    qual_id = models.ForeignKey(JobDetails,on_delete=models.CASCADE,null=True,default=1)
    education = models.CharField(max_length=255, choices=quali)
    experience = models.CharField(max_length=255)
    
    def __str__(self):
        return self.education

class Resumeupload(models.Model):
    document = models.FileField(upload_to='documents/')

    # def __str__(self):
    #     return self.document


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, blank=False, unique=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    

class Subscription(models.Model):
    email = models.CharField(max_length=255, blank=False, unique=True)
    user = models.ForeignKey(Subscriber, related_name="subscriptions", on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, related_name="Jobpost", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email