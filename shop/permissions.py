from rest_framework.permissions import BasePermission


class IsCreatorReadOnlyPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONs']:
            return True
        return obj.created_by == request.user

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONs']:
            return True
        return super().has_permission(request, view)
