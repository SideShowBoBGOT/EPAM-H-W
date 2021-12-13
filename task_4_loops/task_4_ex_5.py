def get_digits(*args):
    """
    Function which receives
    arbitrary amount of arguments and returns
    a tuple of digits of given integers.
    @param args: elements of further tuple
    @return: tuple of given elements
    """
    result_list = []
    if args:
        for el in args:
            for ele in str(el):
                result_list.append(int(ele))
    return tuple(result_list)

