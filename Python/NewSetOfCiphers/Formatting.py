def createMarkup(word:str):
    markup = []
    for letter in word:
        if letter == " ":
            markup.append(0)
        elif letter.isupper():
            markup.append(2)
        elif letter.isupper() == False:
            markup.append(1)
    return markup

def format(markup:list, word:str):
    formatted = []
    for i in range(len(markup)):
        if markup[i] == 0:
            formatted.append(" ")
        elif markup[i] == 1:
            formatted.append(word[i].lower())
        elif markup[i] == 2:
            formatted.append(word[i].upper())
    return "".join(formatted)

def strListToIntList(oldList:list):
    return [int(number) for number in oldList]

def intListToStrList(oldList:list):
    return [str(number) for number in oldList]

def listToString(oldList:list):
    return "".join(oldList)

def equalWords(primaryWord:str, secondaryWord:str):
    firstLength = len(primaryWord)
    secondLength = len(secondaryWord)
    newWord = []
    count = 0
    
    if firstLength != secondLength:
        secondaryWord = secondaryWord.replace(" ", "")
        for i in range(firstLength):
            if secondLength == i - count:
                count = len(secondaryWord) + count
            if primaryWord[i] != " ":
                newWord.append(secondaryWord[i - count])
            else:
                newWord.append(" ")
                count += 1
        return "".join(newWord)      
    elif firstLength == secondLength:
        return secondaryWord
    
def saveInFile(content:str):
    with open("Cipher_File", "w") as CF:
        CF.write(str(content))

def mergeSaveListInFile(contents:list):
    with open("Cipher_File", "w") as CF:
        for content in contents:
            CF.write(content)

def saveListInFile(contents:list):
    with open("Cipher_File", "w") as CF:
        for content in contents:
            CF.write(content)
            CF.write("\n")