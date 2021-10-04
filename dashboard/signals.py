from django.dispatch import Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobPost, Subscriber
from .views import mail_letter

@receiver(post_save, sender=JobPost)
def post_save_create_email(sender, instance,created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if created:
        JobPost.objects.create()
        # mail_letter
        




# new_subscriber = Signal(providing_args=["job", "subscriber"])


