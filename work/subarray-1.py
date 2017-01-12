mylist = [-2,2,3,4,-7]

def mssl(x):
    max_ending_here = max_so_far = 0
    for a in x:
        max_ending_here = max(0, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)
        print "a = " + str(a)
        print "max_so_far = " + str(max_so_far)
        print "max_ending_here = " + str(max_ending_here)
    return max_so_far

def main():
    biggest = mssl(mylist)
    print biggest


if __name__ == "__main__":
    main()
