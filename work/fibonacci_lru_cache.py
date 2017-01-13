
from repoze.lru import lru_cache

@lru_cache(maxsize=500)
def fib(n):
    if n == 1:
        return(1)
    if n == 2:
        return(1)
    elif n > 2 :
        return( fib(n-1) + fib(n-2))



def main():
    for n in range(1,111):
        print fib(n)


if __name__ == "__main__" :
    main()
