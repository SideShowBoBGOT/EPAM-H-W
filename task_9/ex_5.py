def count_letters(s: str):
    characters = list(map(lambda x: x, s))
    uni_characters = set(characters)
    result = dict()
    for u_char in uni_characters:
        count = s.count(u_char)
        result[u_char] = count
    return result

print(count_letters('hello'))
