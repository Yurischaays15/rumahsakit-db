from django.urls import path
from . import views
from .users import urls as user_url
from .poliklinik import urls as poli_url
from .antrian import urls as antrian_url
from .pasien import urls as pasien_url
from .pendaftaran import urls as pendaftaran_url
from django.conf.urls import include
urlpatterns = [
    path('nyoba/', views.TestServer.as_view()),
    path('user/', include(user_url)),
    path('poliklinik/', include(poli_url)),
    path('antrian/', include(antrian_url)),
    path('pasien/', include(pasien_url)),
    path('pendaftaran/', include(pendaftaran_url)),
]
