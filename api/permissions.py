from rest_framework import permissions


class IsAirportOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_airport

class IsAirport(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_airport

