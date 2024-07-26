import CesarCipher as cc, Replacement3x4 as rep, Formatting as f

class Mode:
    def __init__(self):
        pass

    @staticmethod
    def firstMode(saveInFile=True):
        saveInFile = True if input("Save the result to a file, Yes or Not: ").upper()[:1] == "Y" else False

        result = []

        choices = input("[CC] - Cesar Cipher\n[REP] - Replacement 3x4\nEnter your choice, to choose more than one option enter separated by a space: ").upper().split()

        for choice in choices:
            if choice == "CC":
                primaryWord, secondaryWord = input("Enter a primary word and a secondary word, separated by a comma: ").split(",")[:2]
                
                if secondaryWord[0] == " ":
                    secondaryWord = secondaryWord[1:]
                

                Cesar = cc.CesarCipher(primaryWord, secondaryWord)

                option = input("Options:\n[E] - Encrypt\n[D] - Deciphe\nEnter your choice: ")

                result.append(Cesar.cesarCipher(option, saveInFile=False, overwritePrimaryWord=False))

            elif choice == "REP":
                word = input("Enter a word: ")

                Replacement = rep.Replacement(word)
                result.append(Replacement.letterToNumber(overwriteWord=False))

        if saveInFile:
            f.saveListInFile(result)

        return result


    def returnMode(self, chosenMode:str):
        chosenMode = chosenMode.upper()[:1]

        if chosenMode == "F":
            return Mode.firstMode
        
        else:
            print("Invalid choice!")