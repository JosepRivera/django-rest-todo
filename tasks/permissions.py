from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permite editar/eliminar solo al dueño de la tarea.
    """

    def has_object_permission(self, request, view, obj):
        return obj.dueño == request.user
