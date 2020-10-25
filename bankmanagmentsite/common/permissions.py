from rest_framework.permissions import BasePermission
from common.constants import UserType

class IsBranchAdmin(BasePermission):
    message ={'error': 'user is not branch admin'}

    def has_permission(self, request, view):
        if request.user.user_type == UserType.branch_admin:
            return True
        else:
            return False