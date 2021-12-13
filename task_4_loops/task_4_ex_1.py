def swap_quotes(s: str) -> str:
    """
    Function which receives a s and
    replaces all " symbols with ' and vise versa.
    @param s: string
    @return: modified string
    """
    for i in range(len(s)):
        if s[i] == "'":
            prev_s = s
            s = s[:i] + '"'
            try:
                s += prev_s[i + 1:]
            except:
                pass
        else:
            if s[i] == '"':
                prev_s = s
                s = s[:i] + "'"
                try:
                    s += prev_s[i + 1:]
                except:
                    pass

    return s


print(swap_quotes('I don"t know'))