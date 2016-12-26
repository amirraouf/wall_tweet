import hashlib, random

from django.core.mail import send_mail
from django.template import Context
from django.template.backends.django import Template

from wall.settings import EMAIL_HOST_USER, STATIC_ROOT


def generate_activation_key(username):
    rand_integer = str(random.random()).encode('utf-8')
    rand = hashlib.sha1(rand_integer).hexdigest()[:5]
    username = username.encode('utf-8')
    rand = rand.encode('utf-8')
    activation_key = hashlib.sha1(rand + username).hexdigest()
    return activation_key


def send_activation_code_email(data):
    link = "http://127.0.0.1:8080/activate/" + data['activation_key']
    c = Context({'activation_link': link, 'username': data['username']})
    f = open(STATIC_ROOT + data['email_path'], 'r')
    t = Template(f.read())
    f.close()
    message = t.render(c)
    send_mail('Verification Code - Wall app', message, EMAIL_HOST_USER, [data['email']],
              fail_silently=False)