from rest_framework.permissions import BasePermission

class IsAuthorOrSuperuser(BasePermission):
    '''Giving acces to API requests only for superusers or authors of tasks'''
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user == request.user
