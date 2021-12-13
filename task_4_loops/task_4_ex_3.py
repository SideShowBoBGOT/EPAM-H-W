def split_alternative(str_to_split: str, delimiter=' ') -> list:
    """
    Function that splits string by a given delimiter
    @param str_to_split: string
    @param delimiter: pattern according to which the string is split
    @return: list of stings
    """
    try:
        if (not isinstance(delimiter, str)) or (not isinstance(str_to_split, str)):
            if not delimiter:
                pass
            else:
                raise ValueError
        if delimiter == '':
            raise ValueError
        result = []
        if not delimiter in str_to_split:
            result.append(str_to_split)
        while delimiter in str_to_split:
            for index in range(len(str_to_split)):
                if str_to_split[index] == delimiter:
                    copstr = str_to_split
                    str_to_split = str_to_split[:index]
                    result.append(str_to_split)
                    try:
                        str_to_split = copstr[index + 1:]
                        if not delimiter in str_to_split:
                            result.append(str_to_split)
                    except:
                        pass
                    break
        return result
    except ValueError as ex:
        raise ex
