from django.conf import settings
from rest_framework import permissions


class AdminOnlyPermission(permissions.IsAuthenticated):
    message = 'Only Admins allowed.'

    def has_permission(self, request, view):
        if super(AdminOnlyPermission, self).has_permission(request, view):
            return request.user.username == 'admin'

        return False