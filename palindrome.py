"""
A Palindorm (if i am spelling it right) is a function that checks to 
see if a string has the same characters at index x and index -x are the same.
"""

def palindrome(word):
	mid_point = len(word) /2

	for index, char in enumerate(word):

		#print char, word[-index -1]

		if char != word[-index -1]:
			return False

	return True
