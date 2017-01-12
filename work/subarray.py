

mylist = [2,2,-3,4,7]
answer_list = []
interim_list = []
biggest = 0

def build_answer_list(inList):
    if len(inList) == 0:
        return ['']
    print inList

    for j in range(len(inList)):
       if inList not in answer_list and len(inList) > 0 :
          answer_list.append(inList)
    build_answer_list(inList[1:len(inList)])

def main():
     global biggest
     for i in range(len(mylist)):
         for j in range(len(mylist)+ 1):
             if len(mylist[i:j]) > 0 :
                 # print mylist[i:j]
                 build_answer_list(mylist[i:j])



     print "=================   the end =========="

     for answer in answer_list :
        print "answer = "
        print answer
        mysum = sum(answer)
        print "sum = " + str(mysum)
        if mysum > biggest :
            biggest = mysum
            print "biggest =" + str(biggest)

     print "in the end the biggest is: " + str(biggest)




if __name__ == "__main__":
    main()

