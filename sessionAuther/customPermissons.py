from rest_framework.permissions import BasePermission
from rest_framework import permissions

class MyCustomPermissions(BasePermission):
    message = 'Adding students  is not available'

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS :
            return True
        else:
            return False
        # return super().has_permission(request, view)
