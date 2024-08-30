from django.db import models

# Create your models here.
# we are using inbuilt User Model



#generating tokens-----------------: if you want every user to have an automatically generated Token, you can simply catch the User's post_save signal.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)