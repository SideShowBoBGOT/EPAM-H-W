def get_pairs(lst: list) -> list:
    """
    Function which takes a list of elements and returns
    a list of tuples containing pairs of this elements.
    @param lst: list of elements
    @return: list of tuples
    """
    result = None
    if len(lst) > 1:
        result = []
        for i in range(len(lst)):
            try:
                result.append((lst[i], lst[i+1]))
            except:
                pass
    return result

