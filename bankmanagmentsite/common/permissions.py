from rest_framework.permissions import BasePermission
from common.constants import UserType

class IsRegisterConfirmed(BasePermission):
    message = {'error':'user is not confirmed his/her registration'}

    def has_permission(self, request, view):
        if request.user.registration_status:
            return True
        else:
            return False

class IsBranchAdmin(BasePermission):
    message ={'error': 'user is not branch admin'}

    def has_permission(self, request, view):
        if request.user.user_type == UserType.branch_admin:
            return True
        else:
            return False