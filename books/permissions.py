from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Dekhne ki ijazat sab ko hai (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Edit/Delete ki ijazat sirf owner ko hai
        return obj.owner == request.user