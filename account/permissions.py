from rest_framework import permissions


class IsSimpleUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.user_type
        return user_role == 'User'

    def has_object_permission(self, request, view, obj):
        user_role = request.user.user_type
        return user_role == 'User'


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.user_type
        return user_role == 'Moderator'

    def has_object_permission(self, request, view, obj):
        user_role = request.user.user_type
        return user_role == 'Moderator'


class IsAkim(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.user_type
        return user_role == 'Akimat'

    def has_object_permission(self, request, view, obj):
        user_role = request.user.user_type
        return user_role == 'Akimat'
