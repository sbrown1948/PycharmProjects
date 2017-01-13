
from repoze.lru import lru_cache

@lru_cache(maxsize=500)
def fib(n):
    #   check input
    if type(n) != int :
        raise TypeError("n must be a positive integer")
    if type(n) < 1  :
        raise TypeError("n must be a positive integer")
    if n == 1:
        return(1)
    if n == 2:
        return(1)
    elif n > 2 :
        return( fib(n-1) + fib(n-2))



def main():
    for n in range(1,7):
        print "n + 1 result ="
        print (fib(n+1) )
        print "n result = "
        print (fib(n))
        print (float(fib(n+1)) / float(fib(n)))


if __name__ == "__main__" :
    main()
