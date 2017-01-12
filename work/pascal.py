



def pascals_triangle(n_rows):
    results = [] # a container to collect the rows
    row = []
    for _ in range(n_rows):
        row = [1] # a starter 1 in the row
        if results: # then we're in the second row or beyond
            last_row = results[-1] # reference the previous row
            # this is the complicated part, it relies on the fact that zip
            # stops at the shortest iterable, so for the second row, we have
            # nothing in this list comprehension, but the third row sums 1 and 1
            # and the fourth row sums in pairs. It's a sliding window.
            # row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            myzip = zip(last_row, last_row[1:])
            # print myzip
            # print len(myzip)
            for pair in myzip :
                print pair
                # print row
                mysum = sum(pair)
                print mysum
                row.append(mysum)


            # finally append the final 1 to the outside
            row.append(1)
            # print myzip

        results.append(row) # add the row to the results.
    return results

def main():
    triangle_list  = pascals_triangle(5)
    for row in triangle_list :
        print row

if __name__ == "__main__":
    main()