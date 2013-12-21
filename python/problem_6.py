from summations import *

def main(n=10):
    
    num = numbers(n)
    num2 = square_numbers(n)
    print num, num2
    
    answer = (numbers(n)**2)- square_numbers(n)
    print answer
    
main(100)