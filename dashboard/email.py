from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail

from django.conf import settings


def send_review_email(name, email, review):

    context = {
        'name': name,
        'email': email,
        'review': review,
    }

    email_subject = 'Thank you for your review'
    print('----email body')
    email_body = render_to_string('dashboard/email_message.txt', context)

    email = send_mail(
        print('-----email meaasage'),
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)