

def fib(n):
    if n == 1:
        return(1)
    if n == 2:
        return(1)
    elif n > 2 :
        return( fib(n-1) + fib(n-2))



def main():
    for n in range(1,11):
        print fib(n)


if __name__ == "__main__" :
    main()
