def call_once(function):
    """
    Decorator which runs function once and caches the result. All consecutive calls to
    this function should return cached result no matter the arguments.
    @param function: function to decorate
    @return: wrapped function
    """
    result = None

    def wrapper(*args):
        nonlocal result
        if not result:
            result = function(*args)
        return result

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))

print(sum_of_numbers(112, 62))

print(sum_of_numbers(1100, 777))
