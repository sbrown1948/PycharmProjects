

fib_cache = {}



def fib(n):
    if n in fib_cache :
        return(fib_cache[n])
    if n == 1:
        result = 1
    if n == 2:
        result = 1
    elif n > 2 :
        result = ( fib(n-1) + fib(n-2))
    fib_cache[n] = result
    return result




def main():
    for n in range(1, 100):
        print fib(n)


if __name__ == "__main__" :
    main()
