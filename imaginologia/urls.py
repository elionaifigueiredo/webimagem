from django.urls import path
from . import views

urlpatterns = [
    path('raiox', views.index, name="index"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('display_img/<str:id>', views.display_img, name="display_img"),
]