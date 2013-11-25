"""
The Sieve of Eratosthenes

Steps:

1. Create a consecutive integers from 2 to n

2. Initially, let p equal to 2, the first prime.

3. Starting from p, count up (2p, 3p, 4p, ..., np)

4. Remove the multiple of p's from the list of consecutive integers.

    When done, all of the numbers in the list should be prime.
"""
import time


def eratosthenes(n = 100000):
    
    start = time.clock()
    
    numbers = range(3,n + 1,2)
    numbers.insert(0, 2)
        
    for count, value in enumerate(numbers[1:]):
        
        prime = value
        try:
            yield numbers[count]
        except:
            pass
        
        for index, num in enumerate(numbers[count +1:]):

            if num % prime == 0 and num != prime:
                numbers.remove(num)
                
    endtime = time.clock() - start
    print endtime
    
if __name__ == "__main__":
	for index, prime in enumerate(eratosthenes()):
		print "Index %s: %s" % (index, prime)
                
