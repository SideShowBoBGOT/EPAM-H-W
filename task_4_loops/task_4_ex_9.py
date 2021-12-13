def sum_odd_numbers(n: int) -> int:
    """
    Function that For a positive integer n calculates
    the result value, which is equal to the sum
    of the odd numbers of n.
    @param n: positive integer
    @return: sum of the odd numbers of n
    """
    if isinstance(n, bool):
        raise TypeError
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise TypeError
    sum = 0
    for el in str(n):
        if int(el) % 2 == 1:
            sum += int(el)
    return sum

