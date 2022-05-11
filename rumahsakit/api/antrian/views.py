from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Antrian

class GetAntrianNow(APIView):
    def get(self, request, searchId):
        try:
            antrian = Antrian.objects.get(poliklinik__kode=searchId)
            p = {
                'status': 'OK',
                'antrian': antrian.nomor,
            }
            return Response(p)
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })


class AddAntrian(APIView):
    def get(self, request, searchId):
        try:
            antrian = Antrian.objects.get(poliklinik__kode=searchId)
            antrian.nomor += 1
            antrian.save()
            p = {
                'status': 'OK',
                'antrian': antrian.nomor,
            }
            return Response(p)
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })


class ReduceAntrian(APIView):
    def get(self, request, searchId):
        try:
            antrian = Antrian.objects.get(poliklinik__kode=searchId)
            antrian.nomor -= 1
            antrian.save()
            p = {
                'status': 'OK',
                'antrian': antrian.nomor,
            }
            return Response(p)
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })