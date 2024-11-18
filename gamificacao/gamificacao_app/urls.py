from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_selos, name='home'),  # Página inicial
    path('selos/', views.listar_selos, name='listar_selos'),
    path('selos/adicionar/', views.adicionar_selo, name='adicionar_selo'),
]
