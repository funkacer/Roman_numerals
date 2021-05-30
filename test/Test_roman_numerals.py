import unittest

from src.roman_numerals import roman_to_arabic, arabic_to_roman

class KnownValues(unittest.TestCase):
    with open ('Test_cases.tst', 'r') as f:
        lines = f.read().split()
    known_values = []
    for line in lines[1:]:  # first line are column names
        known_values.append((int(line.split(';')[0]), line.split(';')[1]))
        
    def test_arabic_to_roman_known_values(self):
        '''to_roman should give known results with known input'''
        for integer, numeral in self.known_values:
            result = arabic_to_roman(integer)
            self.assertEqual(numeral, result)

    def test_roman_to_arabic_known_values(self):
        '''from_roman should give known results with known input'''
        for integer, numeral in self.known_values:
            result = roman_to_arabic(numeral)
            self.assertEqual(integer, result)
            
if __name__ == '__main__':
    unittest.main()
