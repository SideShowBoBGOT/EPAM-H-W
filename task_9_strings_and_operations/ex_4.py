import string


def chars_in_all(*test_strings):
    """
    Function which receive a changeable number of strings and return
    characters that appear in all strings
    @param test_strings: a collection of strings
    @return: list of characters
    """
    if not test_strings:
        raise ValueError
    for s in test_strings:
        if not isinstance(s, str):
            raise TypeError
    characters = test_strings[0]
    for s in test_strings:
        new_chars = []
        for char in s:
            if char in characters:
                new_chars.append(char)
        characters = ''.join(set(new_chars))

    return set(map(lambda x: x, characters))


def chars_in_one(*test_strings):
    """
    Function which receive a changeable number of strings and return
    characters that appear in at least one string
    @param test_strings: a collection of strings
    @return: list of characters
    """
    if not test_strings:
        raise ValueError
    for s in test_strings:
        if not isinstance(s, str):
            raise TypeError
    return set(map(lambda x: x, ''.join(test_strings)))


def chars_in_two(*test_strings):
    """
    Function which receive a changeable number of strings and return
    characters that appear at least in two strings
    @param test_strings: a collection of strings
    @return: list of characters
    """
    if not test_strings or len(test_strings) < 2:
        raise ValueError
    for s in test_strings:
        if not isinstance(s, str):
            raise TypeError
    characters = list(map(lambda x: x, ''.join(test_strings)))
    uni_characters = set(characters)
    list_of_chars = []
    for uchar in uni_characters:
        char_count = [uchar, 0]
        for char in characters:
            if uchar == char:
                char_count[1] += 1
        list_of_chars.append(char_count)
    result = set()
    for el in list_of_chars:
        if el[1] > 1:
            result.add(el[0])
    return result


def not_used_chars(*test_strings):
    """
    Function which receive a changeable number of strings and return
    characters of alphabet, that were not used in any string
    @param test_strings: a collection of strings
    @return: list of characters
    """
    characters = chars_in_one(*test_strings)
    absent_characters = set()
    for el in string.ascii_lowercase:
        if el not in characters:
            absent_characters.add(el)
    return absent_characters


print(chars_in_all(*["hello", "world", "python", ]))
print(chars_in_one(*["hello", "world", "python", ]))
print(chars_in_two(*["hello", "world", "python", ]))
print(not_used_chars(*["hello", "world", "python", ]))
