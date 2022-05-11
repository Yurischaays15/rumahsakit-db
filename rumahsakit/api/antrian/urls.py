from django.urls import path
from . import views

urlpatterns = [
    path('now/<str:searchId>', views.GetAntrianNow.as_view()),
    path('add/<str:searchId>', views.AddAntrian.as_view()),
    path('reduce/<str:searchId>', views.ReduceAntrian.as_view()),
]