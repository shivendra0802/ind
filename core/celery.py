from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
# app.conf.beat_schedule = {
    
# }

app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=0, minute=46),
        # 'schedule': crontab(hour=0, minute=0, day_of_month=19, month_of_year = 6),
        #'args': (2,)
    }
}



app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')





















# from __future__ import absolute_import, unicode_literals
# import os
# import celery
# from celery import Celery
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# app = Celery('core')
# app.conf.enable_utc = False

# app.conf.update(timezone = 'Asia/Kolkata')

# app.config_from_object(settings, namespace='CELERY')

# # Celery Beat Settings
# # app.conf.beat_schedule = {
    
# # }

# app.autodiscover_tasks()

# # @app.task(bind=True)
# # def debug_task(self):
# #     return True

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))