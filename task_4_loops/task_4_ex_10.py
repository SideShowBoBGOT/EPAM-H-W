import math


def sum_binary_1(n: int):
    """
    Function that for a positive integer n
    calculates the result value, which is equal to the sum of the
    “1” in the binary representation of n otherwise, returns None
    @param n: positive integer
    @return: binary representation of n
    """
    result = []
    res = ''
    if isinstance(n, bool):
        return None
    if not isinstance(n, int):
        return None
    if n <= 0:
        return None
    if n == 1:
        result.append('1')
    if n == 0:
        result.append('0')
    while n != 1 and n != 0:
        result.append(str(n % 2))
        n = math.floor(n / 2)
        if n == 1 or n == 0:
            result.append(str(n))
    result.reverse()
    for el in result:
        res += el
    count = 0
    for el in res:
        if el == '1':
            count += 1
    return count
