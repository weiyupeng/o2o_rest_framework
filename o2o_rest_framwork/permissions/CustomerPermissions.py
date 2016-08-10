from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):

    message = 'you are not Custmer'

    def has_permission(self, request, view):
        if not hasattr(request.user,'engineer') :
            return False
        else:
            print 'NotAssociated'
            return True
class IsOwner(BasePermission):
    message = 'you are not original user'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user