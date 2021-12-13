import string


def is_palindrome(test_string: str) -> bool:
    """
    Function that checks whether a string is a palindrome or not.
    @param test_string: string
    @return: 'True' if it is palindrome, else 'False'
    """
    try:
        ispalin = True
        modstr = ''
        if not isinstance(test_string, str):
            raise ValueError
        for el in test_string:
            if el.upper() in string.ascii_letters.upper():
                modstr += el
        while modstr != '':
            if modstr[0].upper() != modstr[-1].upper():
                ispalin = False
                break
            else:
                modstr = modstr[1:-1]
        return ispalin
    except ValueError as ex:
        raise ex


print(is_palindrome('Aff123a'))
