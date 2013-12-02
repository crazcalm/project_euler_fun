from math import sqrt
import time

def tri(n = 10):
    start = time.clock()
    
    for a in xrange(1,n+1):
        for b in xrange(1, n+1):
            
            c =  a**2 + b**2
            
            if sqrt(c)== int(sqrt(c)):
                #print "%s^2 + %s^2 = %s^2" %(a,b,int(sqrt(c)))
                yield (a,b,int(sqrt(c)))
                
    endtime = time.clock()-start
    print endtime