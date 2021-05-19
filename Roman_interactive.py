import re
import sys

from src.roman_numerals import roman_to_latin, latin_to_roman
from src.check_input import check_input

def main(argv):
    #print(argv)

    #parse argv

    latin, roman = None, None
    
    number = input('Please enter number:\n')

    try:
        latin = int(number)
    except Exception as e:
        roman = number.strip().upper()

    print()
    print(f'Latin: {latin}, Roman: {roman}')

    if latin is not None:
        try:
            roman = latin_to_roman(latin)
            print()
            print(f"Latin {latin} is Roman numeral: {roman}\n")
        except Exception as e:
            print(e, e.__class__.__name__)

    if roman is not None:
        try:
            latin = roman_to_latin(roman)
            print()
            print(f"Roman {roman} is Latin numeral: {latin}\n")
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

        # pass roman/latin number

        latin, roman = None, None
        
        number = input('Please enter number:\n')

        try:
            latin = int(number)
        except Exception as e:
            roman = number.strip().upper()

        #print(latin, roman)

        if roman is not None:
            try:
                latin = roman_to_latin(roman)
                print()
                print(f"Roman {roman} is latin: {latin}\n")
            except Exception as e:
                print(e)

        answer = ''
        while answer not in ['yes','no']:
            answer = input("Do you want to continue? (yes, no):\n").lower()
            answer = check_input(answer, ['yes','no'])

if __name__ == '__main__':
    main(sys.argv[1:])
