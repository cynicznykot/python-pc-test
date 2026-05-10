from unittest import result


def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        # Some action before execution of the original_fn
        print("Executed before function")

        result = original_fn(*args, **kwargs)

        # Some action after execution of the original_fn
        print("Executed after function")

        return result

    return wrapper_function


@decorator_function
def my_function(a, b):
    print("This is my function!")
    return (a, b)

result = my_function(100, 50)
print(result)