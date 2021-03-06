import sys
import argparse

from src.roman_numerals import roman_to_arabic, arabic_to_roman
from src.check_input import check_input


def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='Roman/Arabic', type=str, nargs='*',
                    help='an integer for the accumulator')
    parser.set_defaults(inputs="")

    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--verbose', dest='verbose', action='store_true')
    feature_parser.add_argument('--no-verbose', dest='verbose', action='store_false')
    parser.set_defaults(verbose=False)

    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--interactive', dest='interactive', action='store_true')
    feature_parser.add_argument('--no-interactive', dest='interactive', action='store_false')
    parser.set_defaults(interactive='')

    namespace = parser.parse_args()
    '''
    for k,v in vars(namespace).items():
        print(k, v)
    '''

    if len(vars(namespace)['numbers']) == 0 and isinstance(vars(namespace)['interactive'], str):
        parser.print_help()
        print()
    else:
        print()

    for number in vars(namespace)['numbers']:

        arabic, roman = None, None

        try:
            arabic = int(number)
        except Exception as e:
            roman = number.strip().upper()

        if arabic is not None:
            try:
                result = arabic_to_roman(arabic)
                print(f"Arabic {arabic} is Roman numeral: {result}")
            except Exception as e:
                print(e, e.__class__.__name__)

        elif roman is not None:
            try:
                result = roman_to_arabic(roman)
                print(f"Roman {roman} is Arabic numeral: {result}")
            except Exception as e:
                print(e, e.__class__.__name__)

        print()

    #print(vars(namespace)['interactive'].__class__)
    if vars(namespace)['interactive'] or len(vars(namespace)['numbers']) == 0 and isinstance(vars(namespace)['interactive'], str):

        print("Entering interactive mode. Type q to quit.\n")

        while True:

            # pass roman/arabic number

            arabic, roman = None, None

            answer = input('Please enter number:\n')

            if answer != '':
                answer_check = check_input(answer.lower(), ['quit'], False)
                if answer_check == 'quit':
                    print('\nOK, you have chosen to quit. Bye!\n')
                    break

            number = answer

            try:
                arabic = int(number)
            except Exception as e:
                roman = number.strip().upper()

            if arabic is not None:
                try:
                    roman = arabic_to_roman(arabic)
                    print(f"Arabic {arabic} is Roman numeral: {roman}")
                except Exception as e:
                    print(e, e.__class__.__name__)

            elif roman is not None:
                try:
                    arabic = roman_to_arabic(roman)
                    print(f"Roman {roman} is Arabic numeral: {arabic}")
                except Exception as e:
                    print(e, e.__class__.__name__)

            print()

if __name__ == '__main__':
    main(sys.argv[1:])
