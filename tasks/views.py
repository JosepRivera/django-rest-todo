from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["estado"]
    search_fields = ["titulo", "descripcion"]
    ordering_fields = ["fecha_creacion"]

    def get_queryset(self):
        # solo las tareas del usuario autenticado
        return Task.objects.filter(dueño=self.request.user)

    def perform_create(self, serializer):
        # asignar dueño automáticamente
        serializer.save(dueño=self.request.user)
