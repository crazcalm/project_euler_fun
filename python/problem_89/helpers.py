"""
CheckIO solution for converting numbers into Roman numerals
"""
CHART1 = (("M",1000),("CM", 900) ,("D",500),("CD",400), ("C",100),("XC", 90),
    ("L",50),("XL", 40),("X",10),("IX",9),("V",5), ("IV",4), ("I",1))

CHART2 = (("CM", 900), ("M",1000), ("CD",400), ("D",500), ("XC", 90), ("C",100),
    ("XL", 40), ("L",50), ("IX",9), ("X",10), ("IV",4), ("V",5), ("I",1))

def checkio(data):
    for x,y in CHART1:
        if data - y>=0:
            return x+ checkio(data-y)

    return ""

"""
New Code
"""

def roman_to_number(string):
    #input("\n")
    #print("current string: %s" % string)

    for roman, value in CHART2:
        while string.find(roman) != -1:
            index = string.find(roman)
            length = len(roman)

            #print("Roman: %s, Value: %s, Length: %s" % (roman, value, length))

            if len(string) >=length:
              new_string = string[:index] + string[index + length: ]
              #print("new string: %s" % new_string)
              if len(new_string) == 0:
                  return value
              else:
                  return value + roman_to_number(new_string)

def file_reader(FILE):
    """
    Yields the contents of the file
    """
    with open(FILE, "rt") as f:
        for line in f:
            yield line

if __name__ == "__main__":
    FILE = "roman.txt"
    for index, line in enumerate(file_reader(FILE)):
        print(line)
        if index > 5:
            break

    # 325
    test = "CCCXXV"
    answer = roman_to_number(test)
    print(answer)

    #4999
    test2 = "MMMMCMXCIX"
    answer2 = roman_to_number(test2)
    print(answer2)

    test3 = "IIIIIIIIIIIIIIII"
    answer3 = roman_to_number(test3)
    print(answer3)
    print(checkio(answer3))
