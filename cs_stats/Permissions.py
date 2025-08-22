from rest_framework import permissions
from django.http import Http404
from django.core import exceptions


class BasePermissions(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': ['%(applabel)s.view%(model_name)s'],
        'OPTIONS': ['%(applabel)s.view%(model_name)s'],
        'HEAD': ['%(applabel)s.view%(model_name)s'],
        'POST': ['%(applabel)s.add%(model_name)s'],
        'PUT': ['%(applabel)s.change%(model_name)s'],
        'PATCH': ['%(applabel)s.change%(model_name)s'],
        'DELETE': ['%(applabel)s.delete%(model_name)s'],
    }

    def get_required_object_permissions(self, method, model_cls):
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }
        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        return [perm % kwargs for perm in self.perms_map[method]]

    def has_permission(self, request, view):
        queryset = self._queryset(view)
        model_cls = queryset.model
        user = request.user
        perms = self.get_required_object_permissions(request.method, model_cls)

        if not user.has_perms(perms):
            return False

        return True

    def has_permission_model(self, request, model_cls):

        perms = self.get_required_object_permissions(
            request.method, model_cls)
        user = request.user
        if not user.has_perms(perms):
            return False
        return True