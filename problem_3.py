"""
Question: What is the largest prime factor of the number 600851475143 ?
"""

from prime_sieve import eratosthenes

def main():
	
	number = 600851475143
	stack = [prime for prime in eratosthenes(7000) if number%prime==0]
	print stack

main()
