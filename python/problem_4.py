from palindrome import palindrome

def main():
    stack = [0]
    for x in range(100,1000):
        for y in range(100,1000):
            string = str(x*y)
            
            if palindrome(string):
                if int(stack[0]) < int(string):
                    stack[0] = int(string)
                
    print stack
    
if __name__ == "__main__":
    main()
