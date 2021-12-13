import enum


class SortOrder(enum.Enum):
    ASCENDING = 0,
    DESCENDING = 1


def check_values(lst: [], sort_order: SortOrder):
    """
        The function checks if appropriate values are given

        :param lst: the list of integers
        :param sort_order: the value which tells in which order the list should be sorted
        :return: None
        """
    for el in lst:
        if (not isinstance(el, int)) or isinstance(el, bool):
            raise TypeError
    if (not isinstance(sort_order, SortOrder)) or isinstance(sort_order, bool):
        raise TypeError

    return None


def is_sorted(num_list: list[int], sort_order: SortOrder):
    """
    The function checks if list of integers is sorted in given order

    :param num_list: the list of integers
    :param sort_order: the value which tells in which order the list should be sorted
    :return: True if the list is sorted in given sort_order else False
    """
    check_values(num_list, sort_order)
    for el in num_list:
        if (not isinstance(el, int)) or isinstance(el, bool):
            raise TypeError
    if (not isinstance(sort_order, SortOrder)) or isinstance(sort_order, bool):
        raise TypeError

    result = True
    prev_el = num_list[0]
    if sort_order == SortOrder.ASCENDING:
        for el in num_list[1:]:
            if prev_el > el:
                result = False
                break
            prev_el = el
    if sort_order == SortOrder.DESCENDING:
        for el in num_list[1:]:
            if prev_el < el:
                result = False
                break
            prev_el = el
    return result


def transform(num_list: list[int], sort_order: SortOrder):
    """
    The function replacing the value of each element of an integer list with the sum
    of this element value and its index, only if the given list is sorted in the given order
    (the order is set up by enum value SortOrder).
    :param num_list: the list of integers
    :param sort_order: the value which tells in which order the list should be sorted
    :return: None
    """
    if is_sorted(num_list, sort_order):
        for index, el in enumerate(num_list):
            num_list[index] = index + el
    return None
