def swap_quotes(s: str):
    """
    Function which receives a string and replaces all " symbols with ' and vise versa.
    @param s: string
    @return: modified string
    """
    return s.replace('"', "'")


print(swap_quotes('dsfsdfsdf"sdfsdsd"sdfwqqq""'))
