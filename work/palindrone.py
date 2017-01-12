# A palindrome is something that reads the same backwards and forwards.  The largest palindrome made from the product of any two numbers between 0 and 12 is 121 (11 * 11).
#
#
# Find the largest palindrome made from the product of any two numbers between 0 and 1000.
# 993 * 913 = 906609
#
#
# ecardin@cainc.com
palindrones = []
def main():

    for i in range(12):
        for j in range(12):
            result = i * j
            strResult = str(result)
            if strResult == strResult[::-1]:
                # print result
                palindrones.append(result)
    biggest = 0
    for palindrone in palindrones:
        if palindrone > biggest:
            # print palindrone
            biggest = palindrone

    print "\nbiggest = " + str(biggest)






if __name__ == "__main__":
    main()
