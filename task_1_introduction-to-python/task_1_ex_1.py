import argparse


def calculate(first_num, second_num, operation):
    """
    Function calculates operation on two numbers:
    add, div, mul, sub
    param first_num: first number of operation
    param second_num: second number of operation
    param operation: symbol of operation on numbers
    return: operation result
    """
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '*':
        return first_num * second_num
    elif operation == '/':
        if second_num != 0:
            return first_num / second_num
        else:
            raise ZeroDivisionError
    else:
        raise NotImplementedError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_num', type=float, help='first_num')
    parser.add_argument('operation', type=str, help='operation')
    parser.add_argument('second_num', type=float, help='second_num')
    args = parser.parse_args()
    print(calculate(args.first_num, args.second_num, args.operation))


if __name__ == '__main__':
    main()
