from rest_framework import permissions

class IsProjectOwnerOrMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.visibility == "no_restrictions":
                return request.user.is_authenticated

            return any([request.user == obj.owner, request.user in obj.members.all()])

        return request.user == obj.owner


class IsTaskOwnerOrAssigned(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return any([request.user in obj.project.members.all(), request.user == obj.task_creator])

        return any([obj.task_creator == request.user, obj.assigned_to == request.user])