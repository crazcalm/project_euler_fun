"""
The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

from helpers import file_reader, checkio, roman_to_number, CHART1, CHART2

FILE = "roman.txt"

def optimal_form(string):
    number = roman_to_number(string)
    new_rom = checkio(number)
    return new_rom

def main():

    saved_chars = 0
    for index, line in enumerate(file_reader(FILE)):
        original = line.strip()
        new_version = optimal_form(original)
        print("1: %s\n2: %s" % (original, new_version))
        saved = len(original) - len(new_version)
        print("saved:", saved)
        saved_chars += saved
#        input("\n")
#        if index > 5:
#            break

        print(saved_chars)

if __name__ == "__main__":
    main()
