from django.urls import path

from . import views

app_name= "clases"

urlpatterns = [
    path('listar-todos/', views.listar_clases, name='listar_clases'),
]