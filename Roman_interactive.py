import re

import sys
import traceback

from src.rounding import rd
from src.check_input import check_input

def main(argv):
    #print(argv)

    #parse argv


    if number is not None and precision is not None:
        print(f'Rounding number {number} with precision {precision}: ' + rd(number, precision) + '\n')
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



        answer = ''
        while answer not in ['yes','no']:
            answer = input("Do you want to continue? (yes, no):\n").lower()
            answer = check_input(answer, ['yes','no'])

if __name__ == '__main__':
    main(sys.argv[1:])
