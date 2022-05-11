from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PasienList.as_view()),
    path('modify/', views.ModifyPasien.as_view()),
    path('detail/<str:medical>', views.GetPasienDetail.as_view()),
    path('delete/<str:medical_record>', views.DeletePasien.as_view()),
]