from django.urls import path
from . import views

urlpatterns = [
    path('daftar/', views.PendaftaranView.as_view()),
    path('latest/', views.GetLatestAntrian.as_view()),
]
