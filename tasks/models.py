from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("progreso", "En Progreso"),
        ("terminado", "Terminado"),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.titulo
