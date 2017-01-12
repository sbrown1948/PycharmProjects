


def main():

    f = open('Gettysburg.txt', 'r')
    leftover = ''
    while True:
        ch=f.read(13)
        new_ch = leftover + ch
        # print new_ch
        for i in range(len(new_ch), -1, -1):
            # print ch[i-1]
            if new_ch[i-1] == ' ':
                print new_ch[0:i]
                leftover = new_ch[i:len(new_ch)]
                # print leftover
                break
        if not ch: break
        # print ch

if __name__ == "__main__" :
    main()
