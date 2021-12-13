def split_by_index(s, indexes):
    """
    Function that splits the `s` by indexes specified in `indexes`.
    @param s: string
    @param indexes: list of indexes
    @return: list of strings
    """
    flag = True
    result = []
    prev_index = 0
    filtered_indexes = []
    for index in indexes:
        if isinstance(index, int):
            if 0 < index < len(s):
                filtered_indexes.append(index)
    if filtered_indexes:
        maxind = max(*filtered_indexes)
        for index in filtered_indexes:
            if flag:
                prev_index = index
                flag = False
                result.append(s[:index])
            if index > prev_index:
                result.append(s[prev_index:index])
                prev_index = index
                if index == maxind:
                    try:
                        result.append(s[index:])
                    except:
                        pass
    else:
        result.append(s)
    return result

