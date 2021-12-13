def remember_result(function):
    """
    Decorator which remembers last result of a function
    @param function: function to decorate
    @return: wrapped function
    """
    prev_result = None

    def wrapper(*args):
        nonlocal prev_result
        print(f"Last result = '{prev_result}'")
        prev_result = function(*args)
        return prev_result

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


sum_list('a', 'b')
sum_list('c', 'd')
sum_list('e', 'f')
