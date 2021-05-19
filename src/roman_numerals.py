import re

def roman_to_latin(roman:str, verbose = False) -> int:

    if not isinstance(roman, str):
        print('roman_to_latin function accepts only string input')
        return None
    
    pattern = "^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"
    
    if not(re.search(pattern, roman)) or roman == "":
        print("roman_to_latin function accepts only valid Roman numerals")
        return None
    else:

        roman_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        latin = 0
        length = len(roman)
        for i in range(length):
            d = 1
            if i > 0:
                if roman[length-i-1:length-i+1] in ["IV", "IX", "XL", "XC", "CD", "CM"]: d = -1    # I will diminish the latin number
            d *= roman_values[roman[-i-1]]
            latin += d
            
            #print (length-i-1,a[length-i-1:length-i+1],d,x)

    return latin
