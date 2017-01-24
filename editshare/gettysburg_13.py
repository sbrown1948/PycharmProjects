def main():
    f = open('Gettysburg.txt', 'r')
    leftover = ''
    while True:
        leftover_len = len(leftover)
        num2read = 14 - leftover_len
        ch = f.read(num2read)
        new_ch = leftover + ch
        # print new_ch
        for i in range(len(new_ch), -1, -1):
            # print ch[i-1]

            if new_ch[i - 1] == ' ' :
                print new_ch[0:i]
                leftover = new_ch[i:len(new_ch)]
                break
        if not ch: break
        # print ch
    print leftover

if __name__ == "__main__":
    main()
