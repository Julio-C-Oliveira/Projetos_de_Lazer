import Formatting as f

class CesarCipher:
    def __init__(self, primaryWord:str, secondaryWord:str="SOX"):
        self.primaryWord = primaryWord
        self.secondaryWord = secondaryWord

    @staticmethod
    def letterToNumber(word:str):
        word = word.upper()
        word = word.replace(" ", "0 ")
        word = word.replace('A','1 ')
        word = word.replace('B','2 ')
        word = word.replace('C','3 ')
        word = word.replace('D','4 ')
        word = word.replace('E','5 ')
        word = word.replace('F','6 ')
        word = word.replace('G','7 ')
        word = word.replace('H','8 ')
        word = word.replace('I','9 ')
        word = word.replace('J','10 ')
        word = word.replace('K','11 ')
        word = word.replace('L','12 ')
        word = word.replace('M','13 ')
        word = word.replace('N','14 ')
        word = word.replace('O','15 ')
        word = word.replace('P','16 ')
        word = word.replace('Q','17 ')
        word = word.replace('R','18 ')
        word = word.replace('S','19 ')
        word = word.replace('T','20 ')
        word = word.replace('U','21 ')
        word = word.replace('V','22 ')
        word = word.replace('W','23 ')
        word = word.replace('X','24 ')
        word = word.replace('Y','25 ')
        word = word.replace('Z','26 ')

        return word

    @staticmethod
    def addLists(firstList:list, secondList:list):
        result = []

        if len(firstList) == len(secondList):
            for i in range(len(firstList)):
                if firstList[i] + secondList[i] > 26:
                    result.append(firstList[i] + secondList[i] - 26)

                else:
                    result.append(firstList[i] + secondList[i])

            return result

        else:
            print("Error, the length of lists not equal")

    @staticmethod
    def subtractLists(firstList:list, secondList:list):
        result = []

        if len(firstList) == len(secondList):
            for i in range(len(firstList)):
                if firstList[i] - secondList[i] < 1:
                    result.append(26 - (firstList[i] - secondList[i])*(-1))

                else:
                    result.append(firstList[i] - secondList[i])

            return result

        else:
            print("Error, the length of lists not equal")

    @staticmethod
    def numberToLetter(numberListInt:list, numberListStr:list):
        for i in range(len(numberListStr)):
            if numberListInt[i] >= 1 and numberListInt[i] <= 9:
                numberListStr[i] = numberListStr[i].replace('0',' ')
                numberListStr[i] = numberListStr[i].replace('1','A')
                numberListStr[i] = numberListStr[i].replace('2','B')
                numberListStr[i] = numberListStr[i].replace('3','C')
                numberListStr[i] = numberListStr[i].replace('4','D')
                numberListStr[i] = numberListStr[i].replace('5','E')
                numberListStr[i] = numberListStr[i].replace('6','F')
                numberListStr[i] = numberListStr[i].replace('7','G')
                numberListStr[i] = numberListStr[i].replace('8','H')
                numberListStr[i] = numberListStr[i].replace('9','I')

            elif numberListInt[i] >= 10 and numberListInt[i] <= 26:
                numberListStr[i] = numberListStr[i].replace('10','J')
                numberListStr[i] = numberListStr[i].replace('11','K')
                numberListStr[i] = numberListStr[i].replace('12','L')
                numberListStr[i] = numberListStr[i].replace('13','M')
                numberListStr[i] = numberListStr[i].replace('14','N')
                numberListStr[i] = numberListStr[i].replace('15','O')
                numberListStr[i] = numberListStr[i].replace('16','P')
                numberListStr[i] = numberListStr[i].replace('17','Q')
                numberListStr[i] = numberListStr[i].replace('18','R')
                numberListStr[i] = numberListStr[i].replace('19','S')
                numberListStr[i] = numberListStr[i].replace('20','T')
                numberListStr[i] = numberListStr[i].replace('21','U')
                numberListStr[i] = numberListStr[i].replace('22','V')
                numberListStr[i] = numberListStr[i].replace('23','W')
                numberListStr[i] = numberListStr[i].replace('24','X')
                numberListStr[i] = numberListStr[i].replace('25','Y')
                numberListStr[i] = numberListStr[i].replace('26','Z')

        return numberListStr

    def cesarCipher(self, choice:str="E", saveInFile:bool=True, overwritePrimaryWord:bool=False):
        choice = choice[:1].upper()
        primaryWord = self.primaryWord

        markup = f.createMarkup(primaryWord)
        secondaryWord = f.equalWords(primaryWord, self.secondaryWord)
        
        primaryWord, secondaryWord = [CesarCipher.letterToNumber(word) for word in [primaryWord, secondaryWord]]

        listPrimaryWord, listSecondaryWord = [word.split() for word in [primaryWord, secondaryWord]]

        listPrimaryWord, listSecondaryWord = [f.strListToIntList(oldList) for oldList in [listPrimaryWord, listSecondaryWord]]

        if choice == "E":
            
            resultListInt = CesarCipher.addLists(listPrimaryWord, listSecondaryWord)

        elif choice == "D":
            resultListInt = CesarCipher.subtractLists(listPrimaryWord, listSecondaryWord)

        else:
            print("Invalid input")
            resultListInt = CesarCipher.addLists(listPrimaryWord, listSecondaryWord)
        print(resultListInt)
        resultListStr = f.intListToStrList(resultListInt)

        resultList = CesarCipher.numberToLetter(resultListInt, resultListStr)
        result = f.listToString(resultList)
        result = f.format(markup, result)

        if saveInFile:
            f.saveInFile(result)

        if overwritePrimaryWord:
            self.primaryWord = result

        return result

      