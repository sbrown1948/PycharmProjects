


#
#   count the number of occurences of small array in big_array
big_array = "zxvabcpouabcmnbbbbabcnbv"
small_array = "abc"
indexes = set()

def main():
    offset = -1
    mylen = len(big_array)
    for n in range(0,mylen):
        try:
            offset = big_array.index(small_array,n)
            indexes.add(offset)
        except:
            print "except"




    print("the index numbers are {}".format(indexes))





if __name__ == "__main__":
    main()
