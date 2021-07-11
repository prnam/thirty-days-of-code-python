# Enter your code here. Read input from STDIN. Print output to STDOUT
def fancyDisplay(stringList):
    for item in stringList:
        newString = ""
        lengthOfString = len(item)
        for i in range(lengthOfString):
            if i % 2 == 0:
                newString = newString+item[i]
        newString = newString+" "
        for i in range(lengthOfString):
            if i % 2 != 0:
                newString = newString+item[i]
        print(newString)
    return


if __name__ == '__main__':
    numberofStrings = int(input())
    stringList = []
    for item in range(numberofStrings):
        string = str(input())
        stringList.append(string)
    fancyDisplay(stringList)
