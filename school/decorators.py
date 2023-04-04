from django.contrib.auth.decorators import user_passes_test


def my_admin_decorator(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 1:
            return function(request, *args, **kwargs)
        else:
            return None
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def my_teacher_decorator(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 3:
            return function(request, *args, **kwargs)
        else:
            return None
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def my_student_decorator(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 2:
            return function(request, *args, **kwargs)
        else:
            return None
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap