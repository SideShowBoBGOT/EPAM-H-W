import argparse
import operator
import itertools


def check_formula(user_input: str):
    """
    Function checks formula for EBNF syntax
    and returns operation result.
    @param user_input: formula given by the user
    @return: result of the formula
    """
    result = None
    bool_result = False
    if user_input is not None:
        flag = True
        operators = []
        integers = []
        for el in user_input:
            if el == '+':
                operators.append('add')
            if el == '-':
                operators.append('sub')
            if not (el.isdigit() or el == '+' or el == '-'):
                flag = False
        if flag:
            if not operators:
                result = int(user_input)
                bool_result = True
            else:
                for mixed_el in user_input.split('+'):
                    for integer in mixed_el.split('-'):
                        if integer != '':
                            integers.append(integer)
                if len(integers) == len(operators) + 1:
                    if len(integers) == 2:
                        result = eval(f'operator.{operators[0]}({integers[0]}, {integers[1]})')
                        bool_result = True
                    else:
                        result = integers[0]
                        for operation, integer in itertools.zip_longest(operators, integers[1:]):
                            result = eval(f'operator.{operation}({result}, {integer})')
                            bool_result = True
                else:
                    result = None
                    bool_result = False
    if result == '':
        result = None
        bool_result = False
    return bool_result, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_input', nargs='?', default=None, type=str)
    args = parser.parse_args()
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
