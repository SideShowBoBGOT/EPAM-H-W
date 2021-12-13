def check_values(a1: float, t: float, n: int):
    """
    The function checks if appropriate values are given

    :param a1: the first member of arithmetic sequence
    :param t: the step of arithmetic sequence between two elements
    :param n: the number of members of arithmetic sequence
    :return: None

    """
    if isinstance(a1, bool) or isinstance(t, bool) or isinstance(n, bool):
        raise TypeError
    if not (isinstance(a1, float) or isinstance(t, float) or isinstance(n, int)):
        raise TypeError
    return None


def arithm_progression_product(a1: float, t: float, n: int):
    """
    The function outputing the product of multiplying elements of arithmetic progression sequence.
    :param a1: the first member of arithmetic sequence
    :param t: the step of arithmetic sequence between two elements
    :param n: the number of members of arithmetic sequence
    :return: if the product of all members
    """
    check_values(a1, t, n)
    if isinstance(a1, bool) or isinstance(t, bool) or isinstance(n, bool):
        raise TypeError
    if not (isinstance(a1, float) or isinstance(t, float) or isinstance(n, int)):
        raise TypeError
    sequence = []
    for i in range(n):
        sequence.append(a1 + i * t)
    product = 1
    for element in sequence:
        product *= element
    return product
