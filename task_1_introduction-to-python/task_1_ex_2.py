import argparse
import math
import operator


def calculate(operation, first_num, second_num):
    """
    Function that performs the standard math functions on the data:
    the standard mathematical, logical and comparison functions
    from the built-in libraries.
    param operation: symbol of operation on numbers
    param first_num: first number of operation
    param second_num: second number of operation
    return: operation result
    """
    try:
        return eval(f'{operation}({first_num})')
    except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
        try:
            return eval(f'math.{operation}({first_num})')
        except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
            try:
                return eval(f'operator.{operation}({first_num})')
            except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
                try:
                    return eval(f'{operation}({first_num}, {second_num})')
                except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
                    try:
                        return eval(f'math.{operation}({first_num}, {second_num})')
                    except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
                        try:
                            return eval(f'operator.{operation}({first_num}, {second_num})')
                        except (NotImplementedError, TypeError, AttributeError, NameError, ValueError) as ex:
                            raise ex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', help='Operation')
    parser.add_argument('first_num', help='First number')
    parser.add_argument('second_num', nargs='?', help='Second number', default=None)
    args = parser.parse_args()
    print(calculate(args.operation, args.first_num, args.second_num))


if __name__ == '__main__':
    main()
