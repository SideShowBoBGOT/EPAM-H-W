def check_values(a1: float, t: float, lim: float):
    """
    The function checks if appropriate values are given

    :param a1: the first member of arithmetic sequence
    :param t: the step of arithmetic sequence between two elements
    :param lim: the limit representing the number which is smaller than any element of the sequence
    :return: None

    """
    if isinstance(a1, bool) or isinstance(t, bool) or isinstance(lim, bool):
        raise TypeError
    if not (isinstance(a1, float) or isinstance(t, float) or isinstance(lim, float)):
        raise TypeError
    if not (0 < t < 1):
        raise ValueError
    return None


def sum_geometric_elements(a1: float, t: float, lim: float):
    """
    The function determining the sum of the first elements of a decreasing geometric progression of real
    numbers with a given initial element of a progression `a` and a given progression step `t`,
    while the last element must be greater than a given `lim`.

    :param a1: the first member of arithmetic sequence
    :param t: the step of arithmetic sequence between two elements
    :param lim: the limit representing the number which is smaller than any element of the sequence
    :return: if the sum of all members
    """

    if isinstance(a1, bool) or isinstance(t, bool) or isinstance(lim, bool):
        raise TypeError
    if not (isinstance(a1, float) or isinstance(t, float) or isinstance(lim, float)):
        raise TypeError
    if not (0 < t < 1):
        raise ValueError

    sequence = []
    i = 0
    while True:
        member = a1 * pow(t, i)
        if member > lim:
            sequence.append(member)
            i += 1
        else:
            break
    sum = 0
    for element in sequence:
        sum += element
    return round(sum, 3)



