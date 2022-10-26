from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('usuario', views.cards, name="usuario")
]
