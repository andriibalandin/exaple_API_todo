from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    '''Giving acces to API requests only for owners of tasks'''
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
