from django.db import models

from ..poliklinik.models import Poliklinik


class Antrian(models.Model):
    poliklinik = models.OneToOneField(
        Poliklinik, on_delete=models.CASCADE, related_name='antrian_poli')
    nomor = models.IntegerField()
