import argparse


def new_indexed_list(booll_list: [], common_list: []):
    """
    Function creating new arrangements for indexed_list
    @param booll_list: a list of arrangements
    @param common_list: a list of weights 
    @return: new list of arrangements
    """
    n_indexed_list = []
    indexed_list = [*booll_list]
    for el in indexed_list:
        other_index = el[-1] + 1
        ell = [*el]
        ell.reverse()
        for index in range(0, len(common_list)):
            if index >= other_index:
                copy_el = ell[1:]
                copy_el.reverse()
                n_indexed_list.append([*copy_el, common_list[index], index])
    return n_indexed_list


def no_index(indexed_list: []):
    """
    Function that cleans up indexed_list
    from indexes.
    @param indexed_list: list of arrangements of weights 
    @return: new list of arrangements without indexes
    """
    new_indexed_list = []
    for el in indexed_list:
        el.reverse()
        copy_el = el[1:]
        copy_el.reverse()
        el.reverse()
        new_indexed_list.append([*copy_el])
    return new_indexed_list


def bounded_knapsack(args):
    """
    Function that gives the most profitable
    variant of arranging gold in sack
    @param args: list of weights 
    @return: the best arrangement( max sum )
    """
    try:
        capacity = int(args.capacity)
        number = int(args.bars_number)
        if not args.weights:
            raise ValueError
        if capacity < 0 or number < 0:
            raise ValueError
        weights = []
        for el in args.weights:
            if float(el) < 0 or float(el) != int(el):
                raise ValueError
            integer = int(el)
            weights.append(integer)

        if len(weights)!=number:
            raise ValueError

        max_possible_sum = None

        if weights:
            indexed_list = []
            for index in range(len(weights)):
                indexed_list.append([weights[index], index])
            result = []
            for el in weights:
                result.append([el])
            if number == 2:
                result += [weights]
            else:
                for number_of_elements_in_group in range(number - 2):
                    indexed_list_copy = new_indexed_list(indexed_list, weights)
                    result = result + no_index(indexed_list_copy)
                    indexed_list = indexed_list_copy
                result += [weights]
            sums = []
            for el in result:
                sum = 0
                for integer in el:
                    sum += int(integer)
                sums.append(sum)
            normalized_sums = []
            for el in sums:
                if el <= capacity:
                    normalized_sums.append(el)
            normalized_sums.sort()

            if normalized_sums:
                max_possible_sum = normalized_sums[-1]
        return max_possible_sum
    except (ValueError, TypeError) as ex:
        raise ex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', '--capacity', type=int, help='capacity')
    parser.add_argument('-w', '--weights', type=int, nargs='+', help='weights')
    parser.add_argument('-n', '--bars_number', type=int, help='bars_number')
    args = parser.parse_args()
    print(bounded_knapsack(args=args))





if __name__ == '__main__':
    main()
