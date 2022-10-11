import unittest
import os
import sys
import datetime

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from src.roman_numerals import roman_to_arabic, arabic_to_roman

class TestKnownValues(unittest.TestCase):

    with open (os.path.join(SCRIPT_DIR,'test_cases.txtx'), 'r') as f:
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


runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(TestKnownValues)
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
