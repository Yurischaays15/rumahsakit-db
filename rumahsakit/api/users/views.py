from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import People
from rest_framework.authtoken.models import Token
# Create your views here.
from ..pasien.models import Pasien


class CreateUser(APIView):
    def post(self, request):
        try:
            data = request.data
            email = data['email'].strip()
            password = data['password'].strip()
            name = data['name'].strip()
            nik = data['nik'].strip()
            address = data['address'].strip()
            phone = data['phone'].strip()

            user = User.objects.create_user(email, email, password)
            user.profile.name = name
            user.profile.nik = nik
            user.profile.address = address
            user.profile.phone = phone
            user.save()
            return Response({'status': 'OK'})
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })


class UserDetail(APIView):
    def get(self, request):
        people = People.objects.get(user=request.user)
        med_records = ''
        try:
            pasien = Pasien.objects.get(user=request.user)
            med_records = pasien.medical_record
        except Exception as e:
            print('User error', str(e))
            med_records = '-'

        payload = {
            "status": "OK",
            'id': people.id,
            "email": request.user.email,
            "name": people.name,
            "nik": people.nik,
            "address": people.address,
            "phone": people.phone,
            'role': people.role,
            'medical_record': med_records,
        }
        return Response(payload)

    def post(self, request):
        data = request.data
        name = data['name'].strip()
        nik = data['nik'].strip()
        address = data['address'].strip()
        phone = data['phone'].strip()
        people = People.objects.get(user=request.user)
        people.name = name
        people.nik = nik
        people.address = address
        people.phone = phone
        people.save()
        return Response({'status': 'OK'})


class ObtainToken(APIView):
    def post(self, request):
        d = request.data
        email = d['email'].strip()
        password = d['password'].strip()
        print('the username', email, 'password', password)
        user = authenticate(username=email, password=password)
        if user is not None:
            token = Token.objects.get(user=user)
            payload = {
                'status': 'OK',
                'token': token.key
            }
            return Response(payload)
        else:
            payload = {
                'status': 'FAIL',
                'token': '-'
            }
            return Response(payload)


class ResetPassword(APIView):
    def post(self, request):
        d = request.data
        email = d['email'].strip()
        old_pass = d['old_pass'].strip()
        new_pass = d['new_pass'].strip()
        user: User = authenticate(username=email, password=old_pass)
        if user is not None:
            user.set_password(new_pass)
            user.save()
            p = {
                'status': 'OK',
                'message': 'Password berhasil diubah.'
            }
            return Response(p)
        else:
            p = {
                'status': 'FAIL',
                'message': 'Password lama salah.'
            }
            return Response(p)



