"""
Find the sum of all multiples of 3 or 5 below 1000
"""
import time



def main(n=1000):
    
    start = time.clock()
    
    count = 0
    sum = 0
    while count< n:
        
        if count %3==0 or count%5==0:
            
            sum +=count
            #print sum
            
        count+=1
        
    print sum
    
    endtime = time.clock() - start
    print endtime
        
        

if __name__ == "__main__":
    main()
