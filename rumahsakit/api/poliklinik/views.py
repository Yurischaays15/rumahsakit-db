from django.db.models import QuerySet
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poliklinik, JadwalPraktek
import json

from ..antrian.models import Antrian


class PoliList(APIView):
    def get(self, request):
        payload = []
        polis = Poliklinik.objects.all()
        for poli in polis:
            jadwals: QuerySet[JadwalPraktek] = JadwalPraktek.objects.filter(poliklinik=poli)
            j = []
            for jadwal in jadwals:
                p = {
                    'doctor_name': jadwal.doctor_name,
                    'schedule': json.loads(jadwal.schedule)
                }
                j.append(p)
            res = {
                'poliklinik_id': poli.id,
                'poliklinik_name': poli.name,
                'poliklinik_kode': poli.kode,
                'poliklinik_icon': poli.icon,
                'doctors': j,
            }
            payload.append(res)
        return Response(payload)


class AddPoli(APIView):
    def post(self, request):
        d = request.data
        poliklinik_name = d['poliklinik_name'].strip()
        poliklinik_kode = d['poliklinik_kode'].strip()
        poliklinik_icon = d['poliklinik_icon'].strip()
        doctors = d['doctors']
        poli: Poliklinik = Poliklinik(name=poliklinik_name, icon=poliklinik_icon, kode=poliklinik_kode)
        poli.save()
        for doctor in doctors:
            jadwal: JadwalPraktek = JadwalPraktek(poliklinik=poli, doctor_name=doctor['doctor_name'],
                                                  schedule=json.dumps(doctor['schedule']))
            jadwal.save()

        antrian = Antrian(poliklinik=poli, nomor=0)
        antrian.save()
        return Response({'status': 'OK'})

    def put(self, request):
        d = request.data
        id = d['poliklinik_id']
        poliklinik_name = d['poliklinik_name'].strip()
        poliklinik_kode = d['poliklinik_kode'].strip()
        poliklinik_icon = d['poliklinik_icon'].strip()
        doctors = d['doctors']
        poli: Poliklinik = Poliklinik.objects.get(id=id)
        poli.name = poliklinik_name
        poli.kode = poliklinik_kode
        poli.icon = poliklinik_icon
        poli.save()
        old_schedule: QuerySet[JadwalPraktek] = JadwalPraktek.objects.filter(poliklinik=poli)
        for old in old_schedule:
            old.delete()
        for doctor in doctors:
            jadwal: JadwalPraktek = JadwalPraktek(poliklinik=poli, doctor_name=doctor['doctor_name'],
                                                  schedule=json.dumps(doctor['schedule']))
            jadwal.save()
        return Response({'status': 'OK'})
