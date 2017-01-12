from collections import OrderedDict
def main():
    filePath = "Gettysburg.txt"
    wordDict = OrderedDict()
    wordCount = 0

    #Read lines into a list
    file = open(filePath, 'rU')
    for line in file:
        for word in line.split():
            if word in wordDict :
                wordDict[word] = wordDict[word] + 1
            else:
                wordDict[word] = 1





    print sorted(wordDict.items(), key=lambda x:x[1], reverse=True)

if __name__ == "__main__" :
    main()
