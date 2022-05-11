from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

ROLE_PATIENT = 1
ROLE_ADMIN = 2
ROLE_POLI = 3

class People(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    name = models.TextField()
    nik = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    role = models.IntegerField(default=ROLE_PATIENT)

    def __str__(self):
        return self.name + ' - ' + self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            People.objects.create(user=instance)
            Token.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
