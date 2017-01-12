

def triangle(n):
    result = []
    for row in range(n):
        newrow = [1]
        # print "newrow[0] = "
        # print newrow[0]
        # print "row = "
        # print row
        for col in range(1, row+1):
            # print "newrow[col-1] = "
            # print newrow[col-1]
            # print "col - 1 = "
            # print col - 1
            newcell = newrow[col-1] * float(row+1-col)/col
            print "newcell = "
            print newcell
            newrow.append(int(newcell))
            print "newrow = "
            print newrow
        result.append(newrow)
        print "result = "
        print result
    return result


def main():
    myTriangle = triangle(3)
    # for row in myTriangle :
    #     print row

if __name__ == "__main__" :
    main()
