from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method == 'GET'
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):

        return (request.method == 'GET'
                or request.user.is_authenticated and request.user.is_staff
                or request.user == obj.author)
