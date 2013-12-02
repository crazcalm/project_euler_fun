from prime_sieve import eratosthenes

def main(n=105000):
    
    for index, value in enumerate(eratosthenes(n)):
        if index == 10000:
            print value
            
main()