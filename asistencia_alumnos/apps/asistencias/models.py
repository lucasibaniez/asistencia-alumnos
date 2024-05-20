from django.db import models

from apps.clases.models import Clase
from apps.usuarios.models import Usuario

class Asistencia(models.Model): 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="asistencias")