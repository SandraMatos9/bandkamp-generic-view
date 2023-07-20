from rest_framework import permissions
from rest_framework.views import Request, View
from songs.models import Song


class IsAdminSongOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Song
    ) -> bool:
        if request.method in permissions.SAFE_METHODS:
           return True
        return request.user.is_superuser or request.user == obj.user