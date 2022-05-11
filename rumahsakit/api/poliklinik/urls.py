from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PoliList.as_view()),
    path('detail/', views.AddPoli.as_view()),
]
