"""
I am tired and brain dead...
"""

def main(n=12):
    
    stack = [1000000000]
    
    number = 1
    for x in range(3,n+1):
        number *= x
    
    while(number > 20):
        #print "Checking number: ", x
        if mod(number):
            print "passed the mod function: ", number
            if stack[0]>number:
                stack[0]=number
        number -= 1
            
            
    print stack
    
def mod(num,n=20):
    
    #print num, n
    if n == 1:
        return True
    
    if num % n == 0:
        return mod(num, n-1)
    else:
        return False
    
    
main()
print mod(2520,10)