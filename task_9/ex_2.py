def isPalindrome(s: str):
    if not isinstance(s, str):
        raise ValueError
    if s == s[::-1]:
        return True
    else:
        return False