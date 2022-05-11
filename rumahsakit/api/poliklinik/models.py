from django.db import models


class Poliklinik(models.Model):
    name = models.TextField()
    kode = models.TextField()
    icon = models.TextField()


class JadwalPraktek(models.Model):
    poliklinik = models.ForeignKey(Poliklinik, on_delete=models.CASCADE)
    doctor_name = models.TextField()
    schedule = models.TextField()


