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

def latin_to_roman(latin:int, varbose = False) -> str:
    '''convert integer to Roman numeral'''
    if not isinstance(latin, int):
        raise NotIntegerError('non-integers cannot be converted by latin_to_roman')
    if not (0 < latin < 4000):
        raise OutOfRangeError('{latin} is out of range input in latin_to_roman (valid input is 0-4000)')
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            #print('substracting {0} from input, adding {1} to output'.format(integer, numeral))  
    #print(result)
    return result

    
def roman_to_latin(roman:str, varbose = False) -> int:
    '''convert Roman numeral to integer'''

    roman_numeral_pattern = "^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"

    if not isinstance(roman, str):
        raise InvalidRomanFormatError(f'non-strings cannot be converted by roman_to_latin')
    
    if not re.search(roman_numeral_pattern, roman) or roman == "":
        raise InvalidRomanNumeralError(f'"{roman}" is invalid Roman numeral in roman_to_latin (try MCMLXXIV)')
    
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
