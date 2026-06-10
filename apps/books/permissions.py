from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["GET"]:
            return True

        return (
            request.user.is_authenticated and
            (
                request.user.role == "admin" or request.user.is_staff or request.user.is_superuser
            )
        )