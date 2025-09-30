from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    dueño = serializers.ReadOnlyField(source="dueño.username")  # solo lectura

    class Meta:
        model = Task
        fields = ["id", "titulo", "descripcion", "estado", "fecha_creacion", "dueño"]
