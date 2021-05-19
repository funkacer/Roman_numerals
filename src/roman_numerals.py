import re

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass
class InvalidRomanFormatError(TypeError): pass

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

def arabic_to_roman(arabic:int, varbose = False) -> str:
    '''convert integer to Roman numeral'''
    if not isinstance(arabic, int):
        raise NotIntegerError('non-integers cannot be converted by arabic_to_roman')
    if not (0 < arabic < 4000):
        raise OutOfRangeError('{arabic} is out of range input in arabic_to_roman (valid input is 0-4000)')
    result = ''
    for numeral, integer in roman_numeral_map:
        while arabic >= integer:
            result += numeral
            arabic -= integer
            #print('substracting {0} from input, adding {1} to output'.format(integer, numeral))  
    #print(result)
    return result

    
def roman_to_arabic(roman:str, varbose = False) -> int:
    '''convert Roman numeral to integer'''

    roman_numeral_pattern = "^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"

    if not isinstance(roman, str):
        raise InvalidRomanFormatError(f'non-strings cannot be converted by roman_to_arabic')
    
    if not re.search(roman_numeral_pattern, roman) or roman == "":
        raise InvalidRomanNumeralError(f'"{roman}" is invalid Roman numeral in roman_to_arabic (try MCMLXXIV)')
    
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while roman[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
            #print('found', numeral, 'of length', len (numeral), ' adding', integer)
    #print(result)
    return result

'''
print(to_roman(0))
print(from_roman('A'))
'''
