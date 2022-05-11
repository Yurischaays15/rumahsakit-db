from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CreateUser.as_view()),
    path('detail/', views.UserDetail.as_view()),
    path('token/', views.ObtainToken.as_view()),
    path('resetpassword/', views.ResetPassword.as_view()),
]
