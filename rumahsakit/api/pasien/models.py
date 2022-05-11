from django.contrib.auth.models import User
from django.db import models


class Pasien(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='pasien_profile')
    name = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    nik = models.TextField()
    address = models.TextField()
    telp = models.TextField()
    bpjs = models.TextField()
    medical_record = models.TextField()

