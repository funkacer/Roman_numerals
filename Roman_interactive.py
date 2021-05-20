import re
import sys
import argparse

from src.roman_numerals import roman_to_arabic, arabic_to_roman
from src.check_input import check_input


def main(argv):
    #print(argv)

    #parse argv

    parser = argparse.ArgumentParser()
    parser.add_argument('inputs', metavar='Roman/Arabic', type=str, nargs='*',
                    help='an integer for the accumulator')
    parser.set_defaults(inputs="")

    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--verbose', dest='verbose', action='store_true')
    feature_parser.add_argument('--no-verbose', dest='verbose', action='store_false')
    parser.set_defaults(verbose=False)

    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--interactive', dest='interactive', action='store_true')
    feature_parser.add_argument('--no-interactive', dest='interactive', action='store_false')
    parser.set_defaults(interactive=True)


    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

    combined = ChainMap(command_line_args, os.environ, defaults)
    print(combined['color'])
    print(combined['user'])

    '''

    namespace = parser.parse_args()
    for k,v in vars(namespace).items():
        print(k, v)
    

    arabic, roman = None, None
    
    number = input('Please enter number:\n')

    try:
        arabic = int(number)
    except Exception as e:
        roman = number.strip().upper()

    print()
    print(f'Arabic: {arabic}, Roman: {roman}')

    if arabic is not None:
        try:
            roman = arabic_to_roman(arabic)
            print()
            print(f"arabic {arabic} is Roman numeral: {roman}\n")
        except Exception as e:
            print(e, e.__class__.__name__)

    if roman is not None:
        try:
            arabic = roman_to_arabic(roman)
            print()
            print(f"Roman {roman} is arabic numeral: {arabic}\n")
        except Exception as e:
            print(e, e.__class__.__name__)
            
    print("Entering interactive mode.\n")
    answer = ''
    while answer not in ['yes','no']:
        answer = input("Do you want to continue? (yes, no):\n").lower()
        answer = check_input(answer, ['yes','no'])
    if answer != 'yes':
            return None

    answer = 'yes'

    while answer == 'yes':

        # pass roman/arabic number

        arabic, roman = None, None
        
        number = input('Please enter number:\n')

        try:
            arabic = int(number)
        except Exception as e:
            roman = number.strip().upper()

        #print(arabic, roman)

        if roman is not None:
            try:
                arabic = roman_to_arabic(roman)
                print()
                print(f"Roman {roman} is arabic: {arabic}\n")
            except Exception as e:
                print(e)

        answer = ''
        while answer not in ['yes','no']:
            answer = input("Do you want to continue? (yes, no):\n").lower()
            answer = check_input(answer, ['yes','no'])

if __name__ == '__main__':
    main(sys.argv[1:])
