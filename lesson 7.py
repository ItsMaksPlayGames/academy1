def add_prefix_suffix(prefix="", suffix=""):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"{prefix}{result}{suffix}"
        return wrapper
    return decorator

@add_prefix_suffix(prefix="[Start] ", suffix=" [End]")
def greet(name):
    return f"Hello, {name}!"

message = greet("Yatsenko Evgeniy Valerievich")
print(message)

