
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="encode_req"),
    path('v1/', views.code, name="encode_req"),
    path('v1/encode', views.encode_run, name="encode"),
    path('v1/decode', views.decode_run, name="decode"),
]