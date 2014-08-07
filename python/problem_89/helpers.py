"""
CheckIO solution for converting numbers into Roman numerals
"""
def checkio(data):

    #replace this for solution
    chart = (("M",1000),("CM", 900) ,("D",500),("CD",400), ("C",100),("XC", 90),
    ("L",50),("XL", 40),("X",10),("IX",9),("V",5), ("IV",4), ("I",1))

    for x,y in chart:
        if data - y>=0:
            return x+ checkio(data-y)

    return ""
