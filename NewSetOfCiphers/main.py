import CesarCipher as Cesar, Replacement3x4 as Replace, Formatting as F

#primary_word = input("Insira a palavra principal: ")
#secondary_word = input("Insira a palavra secundária: ")
primary_word = "ShiSOX"
secondary_word = "Bleach"
choice = "E"

print(primary_word[:3])

result = []
letter, number = Cesar.CesarCipher(primaryWord=primary_word, secondaryWord=secondary_word).cesarCipher(choice=choice)
number = F.listToString(number)
result.append(f"_{number}-{letter}_")
result.append(letter)
result.append(number)
result.append(Replace.Replacement(primary_word).letterToNumber())

for i in result:
    print(i)

F.saveListInFile(result)