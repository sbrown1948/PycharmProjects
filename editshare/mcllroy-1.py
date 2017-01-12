from collections import Counter
import re
def main():

     words = re.findall(r'\w+', open('Gettysburg.txt').read().lower())
     print Counter(words).most_common(10)

if __name__ == "__main__" :
    main()
