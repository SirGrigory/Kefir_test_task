from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPaginator(PageNumberPagination):
    
    page_size =1
    max_page_size = 2
    
class UserUpdatePermission(BasePermission):
    message = 'Editing info is to user'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user

