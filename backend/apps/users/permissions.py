from functools import wraps
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from graphql_jwt.decorators import login_required

def admin_required(func):
    @wraps(func)
    def wrapper(self, info, *args, **kwargs):
        user = info.context.user
        
        if (not user.is_admin) and (not user.is_superuser):
            raise Exception('You must be an organization admin to perform this action.')
        return func(self, info, *args, **kwargs)
    return wrapper

def staff_required(func):
    @wraps(func)
    def wrapper(self, info, *args, **kwargs):
        user = info.context.user
        
        if (not user.is_staff) and (not user.is_admin) and (not user.is_superuser):
            raise Exception('You must be staff to perform this action.')
        return func(self, info, *args, **kwargs)
    return wrapper