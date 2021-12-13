def count_letters(s: str):
    """
    Function which takes string as an argument
    and returns a dictionary that contains letters of given
    string as keys and a number of their occurrence as values.
    @param s: string
    @return: dictionary of characters and number of their occurrence
    """
    characters = list(map(lambda x: x, s))
    uni_characters = set(characters)
    result = dict()
    for u_char in uni_characters:
        count = s.count(u_char)
        result[u_char] = count
    return result


print(count_letters('hello'))
