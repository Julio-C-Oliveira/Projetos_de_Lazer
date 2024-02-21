class Replacement:
    def __init__(self, word:str):
        self.word = word

    def letterToNumber(self, overwriteWord=False):
        word = self.word
        
        word = word.upper()
        word = word.replace(' ','0')
        word = word.replace('A','2')
        word = word.replace('B','2')
        word = word.replace('C','2')
        word = word.replace('D','3')
        word = word.replace('E','3')
        word = word.replace('F','3')
        word = word.replace('G','4')
        word = word.replace('H','4')
        word = word.replace('I','4')
        word = word.replace('J','5')
        word = word.replace('K','5')
        word = word.replace('L','5')
        word = word.replace('M','6')
        word = word.replace('N','6')
        word = word.replace('O','6')
        word = word.replace('P','7')
        word = word.replace('Q','7')
        word = word.replace('R','7')
        word = word.replace('S','7')
        word = word.replace('T','8')
        word = word.replace('U','8')
        word = word.replace('V','8')
        word = word.replace('W','9')
        word = word.replace('X','9')
        word = word.replace('Y','9')
        word = word.replace('Z','9')

        if overwriteWord:
            self.word = word

        return word

replace = Replacement("Bleach Chii Date Live Zero")
print(replace.letterToNumber())