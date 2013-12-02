from prime_sieve import eratosthenes2

def main(n=2000000):
    
    sum = 0
    for index, value in enumerate(eratosthenes2(n)):
        #print index, value
        sum+= value
        
    print "sum:", sum
    
main()