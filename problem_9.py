from pythagorean_triplet import tri

def main():
    
    for a,b,c in tri(1000):
        if a+b+c == 1000:
            print "Yes"
            print a*b*c
            break
        
main()