import argparse


def calculate(n):
    """
    Function that for a given integer n calculates the value which is equal to a:
    @param n: number
    @return:  - squared number, if its value is strictly positive;
              - modulus of a number, if its value is strictly negative;
              - zero, if the integer n is zero.
    """
    result = None
    if n > 0:
        result = n * n
    elif n < 0:
        result = n * (-1)
    elif n == 0:
        result = 0
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='integer n')
    args = parser.parse_args()
    print(calculate(args.n))


if __name__ == '__main__':
    main()
