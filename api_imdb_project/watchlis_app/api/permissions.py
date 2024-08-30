from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # admin_permission=bool(request.user and request.user.is_staff)
        # return request.method=='GET' or admin_permission
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

class IsReviewUserOrReadOnly(permissions.BasePermission):# if the user is Review owner then we are going to give him a permission to edit. otherwise it going to read only

    #same methods: get 
    #unsafe methods: post delete put

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        # Check permissions for read-only request
        else:
            return obj.review_user==request.user or request.user.is_staff  # here the review can be updated with himself or admin only
        # Check permissions for write request
    