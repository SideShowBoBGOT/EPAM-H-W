def get_longest_word(str_to_parse: str) -> str:
    """
    Function which returns the longest word in the given string.
    @param str_to_parse: string
    @return: string which represents the longest word
    """
    if not isinstance(str_to_parse, str):
        raise ValueError
    words = str_to_parse.split(' ')
    longword = ''
    for el in words:
        if len(longword) < len(el):
            longword = el
    return longword




