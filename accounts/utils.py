from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

import os
import smtplib
from email.message import EmailMessage

def detectUser(user):
    if user.role ==1:
        redirectUrl='vendorDashboard'
        return redirectUrl
    elif user.role ==2:
        redirectUrl='custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl ='/admin'
        return redirectUrl
    
    
def send_verification_email(request,user):
    current_site=get_current_site(request)
    mail_subject="Please activate your account"
    message= render_to_string('accounts/emails/account_verification_email.html', {
        'user' : user,
        'domain': current_site,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token':default_token_generator.make_token(user)
    })
    to_email= 'vivekchauhan14@hotmail.com'  #user.email
    mail= EmailMessage(mail_subject,message, to=[to_email])
    mail.send()
    

def activate_user(request,user):
#credentials
    email_user = 'prabhatidubey@outlook.com'
    email_pass = 'God@1110'

    contacts = ['vivekchauhan14@hotmail.com']
    sender = email_user
    to = contacts

    msg = EmailMessage()
    msg['Subject'] ="Please activate your account"
    msg['From'] = sender
    msg['To'] = ', '.join(contacts)
    msg.set_content('YOUR EMAIL MESSAGE HERE')
    message= render_to_string('accounts/emails/account_verification_email.html', {
        'user' : user,
        'domain': 'http://127.0.0.1:8000',
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token':default_token_generator.make_token(user)
    })
    
    print("message: &&  ** ", message)
    msg.set_content(message)
    try:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
            smtp.starttls()
            smtp.login(email_user, email_pass)
            print("after login ........................")
            smtp.send_message(msg)
    except Exception as e:
        print(e)
    
    

    