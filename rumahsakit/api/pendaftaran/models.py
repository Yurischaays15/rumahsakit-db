from django.db import models
from django.contrib.auth.models import User

from ..poliklinik.models import Poliklinik


class Pendaftaran(models.Model):
    poliklinik = models.ForeignKey(
        Poliklinik, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.TextField()
    hari = models.TextField()
    jam = models.TextField()
    antrian = models.IntegerField()


class AntrianTracker(models.Model):
    first = models.IntegerField()
    second = models.IntegerField()

