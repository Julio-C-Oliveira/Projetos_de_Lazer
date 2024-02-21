# Data de Criação: xx/xx/2022 - Inicio do curso e tentando fazer algo. 

import Mode as m

choice = input("[F] - First Mode\nEnter a mode: ")

Mode = m.Mode()
chosenMode = Mode.returnMode(choice)

print(f"Result: {chosenMode()}")