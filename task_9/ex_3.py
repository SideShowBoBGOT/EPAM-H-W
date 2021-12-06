import re
def get_longest_word(s: str):
    if not isinstance(s, str):
        raise ValueError
    l = re.split(r'[\s]|[^A-Za-z0-9]', s)
    maxs = l[0]
    for a in l:
        if len(maxs)<len(a):
            maxs = a
    return maxs
print(get_longest_word('Python is simple and effective!'))