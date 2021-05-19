
import re

a = ""

while a.strip(" ").lower()!="n":
    a = input("Vložte římskou číslici(N/n=konec):").strip(" ")
    pattern = "^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"
    if not(re.search(pattern,a)) or a=="":
        if a.lower()!="n": print("Toto není platné římské číslo")
        if a.lower()=="n": print("Konec")
    else:
        x=0
        for i in range (len(a)):
            d=1
            if i > 0:
                if a[len(a)-i-1:len(a)-i+1] == "IV" or a[len(a)-i-1:len(a)-i+1] == "IX" or a[len(a)-i-1:len(a)-i+1] == "XL" or a[len(a)-i-1:len(a)-i+1] == "XC" or a[len(a)-i-1:len(a)-i+1] == "CD" or a[len(a)-i-1:len(a)-i+1] == "CM":
                    d=-1
            if a[-i-1]=="I":
                d*=1
            if a[-i-1]=="V":
                d*=5
            if a[-i-1]=="X":
                d*=10
            if a[-i-1]=="L":
                d*=50
            if a[-i-1]=="C":
                d*=100
            if a[-i-1]=="D":
                d*=500
            if a[-i-1]=="M":
                d*=1000
            x+=d
            #print (len(a)-i-1,a[len(a)-i-1:len(a)-i+1],d,x)
        print("Toto je platné římské číslo, arabskými číslicemi to je:", x)
