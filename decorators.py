from functools import wraps


def DemoDecorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("Decorator Call....")
        return f(*args, **kwargs)

    return decorated_function