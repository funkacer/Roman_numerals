import unittest
import os
import sys
import datetime

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from src.roman_numerals import roman_to_arabic, arabic_to_roman
from src.roman_numerals import OutOfRangeError, NotIntegerError, InvalidRomanNumeralError, InvalidRomanFormatError

class TestRaiseError(unittest.TestCase):

    def test_arabic_to_roman_raise_errors(self):
        '''arabic_to_roman should raise error with invalid input'''
        inputs = [1.1, -1.1, "", "A"]
        for input in inputs:
            self.assertRaises(NotIntegerError, arabic_to_roman, input)
        inputs = [0, 4000, -1]
        for input in inputs:
            self.assertRaises(OutOfRangeError, arabic_to_roman, input)

    def test_roman_to_arabic_raise_errors(self):
        '''roman_to_arabic should raise error with invalid input'''
        inputs = [0, 4000, -1, 1.1]
        for input in inputs:
            self.assertRaises(InvalidRomanFormatError, roman_to_arabic, input)
        inputs = ["", "A", "MMMM", "MCMC"]
        for input in inputs:
            self.assertRaises(InvalidRomanNumeralError, roman_to_arabic, input)

runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(TestRaiseError)
result = runner.run(suite)

a = str(datetime.datetime.now()) + '\n'
a += __file__ + '\n'
a += str(result) + '\n'

if result.errors:
    a += 'result::errors' + '\n'
    for item in result.errors:
        for i in item:
            a += str(i)

if result.failures:
    a += 'result::failures' + '\n'
    for item in result.failures:
        for i in item:
            a += str(i)

if result.skipped:
    a += 'result::skipped' + '\n'
    for item in result.skipped:
        for i in item:
            a += str(i)

if result.testsRun:
    a += 'result::testsRun ' + str(result.testsRun) + '\n'

if result.wasSuccessful():
    a += 'TEST(S) SUCCESSFUL!' + '\n'
else:
    a += 'TEST(S) FAILED!!!' + '\n'

try:
    with open (os.path.join(SCRIPT_DIR,'test_roman_numerals_results.txt'), 'r') as file:
        o = file.read()
except Exception as e:
    o = ''

with open (os.path.join(SCRIPT_DIR,'test_roman_numerals_results.txt'), 'w') as file:
        file.write(a+'\n')
        file.write(o)
