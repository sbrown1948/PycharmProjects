from collections import defaultdict
mylist = [-2,2,3,4,-7]

def mssl(lst):
    d = defaultdict(list)
    for i in range(len(lst)+1):
        for j in range(len(lst)+1):
             d[sum(lst[i:j])].append(lst[i:j])
    key = max(d.keys())
    return (key, d[key])




def main():
    biggest = mssl(mylist)
    print biggest


if __name__ == "__main__":
    main()