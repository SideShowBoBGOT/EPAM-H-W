def combine_dicts(*args):
    """
    The function combining dictionaries into one dictionary.
    !!!Note: if keys are equal then values are summarized!!!

    :param args: dictionaries
    :return: result - sum of all dictionaries
    """
    result = dict()
    common_keys = []
    for el in args:
        if result.keys():
            for res_key in result.keys():
                for el_key in el.keys():
                    if res_key == el_key:
                        common_keys.append((res_key, result[res_key]))
            result.update(el)
            for res_key in result.keys():
                for common_key in common_keys:
                    if common_key[0] == res_key:
                        result[res_key] += common_key[1]
        else:
            result.update(el)
        common_keys.clear()
    return result

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
common_dict = combine_dicts(dict_1, dict_2, dict_3)
print(common_dict)