
from django.urls import path

from . import views

urlpatterns = [
    path('', views.code, name="encode_req"),
    path('encode', views.encode_run, name="encode"),
    path('decode', views.decode_run, name="decode"),
]