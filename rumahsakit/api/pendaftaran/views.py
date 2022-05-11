from rest_framework.response import Response
from rest_framework.views import APIView

from ..pendaftaran.models import Pendaftaran, AntrianTracker
from ..poliklinik.models import Poliklinik

class GetLatestAntrian(APIView):
    def get(self, request):
        tanggal = request.query_params.get('tanggal')
        kode_poli = request.query_params.get('kodepoli')
        poliklinik = Poliklinik.objects.get(kode=kode_poli)
        try:
            existing: Pendaftaran = Pendaftaran.objects.filter(tanggal=tanggal).filter(poliklinik=poliklinik).order_by('-antrian')[0]
            antrian = existing.antrian
            return Response({
                'status': 'OK',
                'antrian': antrian
            })
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })


# 100010101
# 100010102
# 100010103



class PendaftaranView(APIView):
    def post(self, request):
        d = request.data
        kode_poli = d['kode_poli']
        tanggal = d['tanggal']
        hari = d['hari']
        jam =d['jam']
        antrian = 0
        poliklinik = Poliklinik.objects.get(kode=kode_poli)
        try:
            existing: Pendaftaran = Pendaftaran.objects.filter(tanggal=tanggal).filter(poliklinik=poliklinik).order_by('-antrian')[0]
            antrian = existing.antrian + 1
        except Exception as e:
            antrian = 1
            print(e)
        result = Pendaftaran(poliklinik=poliklinik, user=request.user, tanggal=tanggal, antrian=antrian, hari=hari, jam=jam)
        result.save()
        return Response({'status': 'OK'})

    def get(self, request):
        tanggal = request.query_params.get('tanggal')
        kode_poli = request.query_params.get('kodepoli')
        try:
            poli = Poliklinik.objects.get(kode=kode_poli)
            result: Pendaftaran = Pendaftaran.objects.filter(poliklinik=poli, user=request.user, tanggal=tanggal)[0]
            res = {
                'status': 'OK',
                'poli': poli.name,
                'tanggal': tanggal,
                'hari': result.hari,
                'antrian': result.antrian,
                'jam': result.jam,
            }
            return Response(res)
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })






