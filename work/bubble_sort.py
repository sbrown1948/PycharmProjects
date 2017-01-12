

def main(alist):
    for passnum in range(len(alist)-1,0,-1):
        print "passnum = " + str(passnum)
        for i in range(passnum):
            print "i = " + str(i)
            print alist
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


    print("=============  done ==========")
    print(alist)



if __name__ == "__main__" :
    my_list = [9,8,7,6,5,4,3,2,1]
    main(my_list)
