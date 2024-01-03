from rest_framework import permissions
from django.contrib.auth import get_user, get_user_model


class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user_pk = request.user.pk
        user = get_user_model().objects.get(pk=user_pk)
        return bool(user.groups.filter(name='author').exists() or user.is_superuser)
