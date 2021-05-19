

import roman
import unittest

class KnownValues(unittest.TestCase):
    known_values = ((1, 'I'),
                    (4, 'IV'),
                    (8, 'VIII'),
                    (13, 'XIII'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman should give known results with known input'''
        for integer, numeral in self.known_values:
            result = roman.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''from_roman should give known results with known input'''
        for integer, numeral in self.known_values:
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)
            
if __name__ == '__main__':
    unittest.main()
