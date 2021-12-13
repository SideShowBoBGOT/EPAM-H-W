from typing import List


def product_array(num_list: List[int]) -> List[int]:
    """
    Function which, given a list of integers,
    returns a new  or modified list
    in which every element at index i of the new list is the product
     of all the numbers in the original array except the one at i.
    @param num_list: list of numbers
    @return: modified list
    """
    result = []
    for i in range(len(num_list)):
        worklist = []
        try:
            worklist = num_list[:i]
        except:
            pass
        try:
            worklist += num_list[i+1:]
        except:
            pass
        mult = 1
        for el in worklist:
            mult*=el
        result.append(mult)
    return result

