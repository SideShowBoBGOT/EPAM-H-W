def fibonacci_loop(seq):
    """
    Function which accepts a list of values and
    prints out values in one line on these conditions:
    - floating point numbers should be ignored
    - string values should stop the iteration
    - loop control statements should be used
    @param seq: list of elements
    @return: None
    """
    for el in seq:
        if not isinstance(el, bool):
            if isinstance(el, int):
                print(el, end=' ')
            if isinstance(el, str):
                break


fibonacci_loop([0, 1, 1.1, 1, 2, 99.9, 3, 0.0, 5, 8, "stop", 13, 21, 34])
