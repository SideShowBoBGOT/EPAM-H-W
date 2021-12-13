import argparse


def from_roman_numerals(args):
    """
    Function that converts roman numbers to numerals
    @param args: string of roman number
    @return: standard numeral
    """
    s = args.n
    for el in s:
        if not el in 'IVXLC':
            raise ValueError
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    if num > 100:
        raise ValueError
    return num


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
