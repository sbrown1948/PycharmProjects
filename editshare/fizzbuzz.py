
def main():
    fizzFlag = 0
    buzzFlag = 0
    fizzBuzzFlag = 0
    for num in range(1,101):
        if num % 3 == 0 :
            fizzFlag = 1
        if num % 5 == 0 :
            buzzFlag = 1
        if num % 3 == 0 and num % 5 == 0 :
            fizzBuzzFlag = 1
        if fizzBuzzFlag == 1:
            print "FizzBuzz" + str(num)
        elif fizzFlag == 1 :
            print "Fizz" + str(num)
        elif buzzFlag == 1 :
            print "Buzz" + str(num)
        else:
            print str(num)
        fizzFlag = 0
        buzzFlag = 0
        fizzBuzzFlag = 0




if __name__ == "__main__" :
    main()
