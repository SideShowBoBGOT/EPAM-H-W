def isPalindrome(s: str):
    """
    Function that checks whether a string is a palindrome or not.
    @param s: string
    @return: True if palindrome, Else False
    """
    if not isinstance(s, str):
        raise ValueError
    if s == s[::-1]:
        return True
    return False
