a = 'global "a"'


def enclosed_function():
    """
    Function that has inner function
    @return: function
    """

    def inner_function():
        """
        Function which is inner function of
        enclosed function
        @return: None
        """
        print('inner_function')

    return inner_function


def enclosing_function_1():
    """
    Function that has inner function
    @return: function
    """
    a = 'enclosed "a"'

    def inner_function():
        """
        Function which is inner function of
        enclosed function
        @return: None
        """
        global a
        print(a)

    return inner_function


def enclosing_function_2():
    """
    Function that has inner function
    @return: function
    """
    a = 'enclosed "a"'

    def inner_function():
        """
        Function which is inner function of
        enclosed function
        @return: None
        """
        nonlocal a
        print(a)

    return inner_function


def main():
    foo = enclosed_function()
    foo1 = enclosing_function_1()
    foo2 = enclosing_function_2()
    foo()
    foo1()
    foo2()


if __name__=='__main__':
    main()