from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path, include

# from .views import login, home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='pagina_principal'),
    path('registrarme/', views.registrarme, name="registrarme"),
    
    
    # path('login/', views.login, name="iniciar_sesion"),
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name="iniciar_sesion"),
    path('logout/', views_django.logout_then_login, name="cerrar_sesion"),

    # Includes
    path("usuarios/", include('apps.usuarios.urls')),
    path("clases/", include('apps.clases.urls')),
    path("asistencias/", include('apps.asistencias.urls'))
]
