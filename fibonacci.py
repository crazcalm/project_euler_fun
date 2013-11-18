"""
Fibonacci numbers


"""
import time

def fibonacci(n=10):
    """
    Computer everything here.
    """
    start = time.clock()
    
    fib_1 = 0
    fib_2 = 1
    
    count = 2
    
    while count <= n:
        
        fib_n = fib_2 + fib_1
        fib_1 = fib_2
        fib_2 = fib_n
        
        count +=1
        
        #print "The %sth fibonacci number is %s" %(count, fib_n)
        
    endtime = time.clock() - start
    
    print "The %sth fibonacci number is %s" %(count, fib_n)
    print endtime
    
    
def fib(n=10):
    """
    Uses generators
    """
    start = time.clock()
    
    fib_1 = 0
    fib_2 = 1
    
    count = 2
    
    while count <= n:
        
        fib_n = fib_2 + fib_1
        fib_1 = fib_2
        fib_2 = fib_n
        
        count +=1
        
        yield fib_n
        
    endtime = time.clock() - start
    
    print "The %sth fibonacci number is %s" %(count, fib_n)
    print endtime
        
        
for num in fib():
    print num
        
if __name__ == "__main__":
    fibonacci()
        
        
        
        