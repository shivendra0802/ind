from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"


from django.contrib.auth import get_user_model

# from celery import shared_task
from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from core import settings
from datetime import timedelta

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time)
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"


# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from celery.decorators import task
# from celery.utils.log import get_task_logger

# from dashboard.email import send_review_email

# logger = get_task_logger(__name__)


# @shared_task
# def add(x,y):
#     print('------ task addede')
#     return x+y

# @task(name="send_review_email_task")
# def send_review_email_task(name, email, review):
#     logger.info("Sent review email")
#     return send_review_email(name, email, review)