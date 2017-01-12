

mystring = 'abc'


def get_permutations(string):
    print "incoming = " + string
    if len(string) == 0:
        return ['']
    # print "string[1:len(string)] = " + string[1:len(string)]
    prevList = get_permutations(string[1:len(string)])
    # print "prevList = "
    # print prevList
    nextList = []
    # print "::::::::::::::::::::"
    print "prevList = "
    print prevList
    print "==============="
    for i in range(0,len(prevList)):
        # print "len of string = "
        # print len(string)
        for j in range(0,len(string)):
        # for j in range(0,3):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            # print "newString = "
            # print newString
            nextList.append(newString)
            # if newString not in nextList:
            #     nextList.append(newString)
            print "********  begin  nextlist ***************"
            print nextList
            print "********  end  nextlist ***************"
    return nextList

permutations = get_permutations(mystring)
print "====================="
for permutation in permutations:
    print permutation

# def place_letter(prefix, letter):
#     newstring = prefix
#     for i in range(len(mystring)-1):
#         newstring.append(letter)
#         print newstring
#
# for i in range(len(mystring)):
#     prefix = mystring[i]
#     print prefix
#     place_letter(prefix, )
#
#     # newstring = prefix + mystring[i:len(mystring)-1]
#     # print newstring


# carray = [c]
# barray = [bc, cb]
# aarray = [abc, bca, bac, bac ]


