is_caracter = lambda c: False if (ord(c) >= 0 and ord(c) <= 32) or (ord(c) >= 127 and ord(c) <= 160) else True
is_lower_caracter = lambda c: True if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 224 and ord(c) <= 382) else False
is_quebra_de_linha = lambda c: True if c == "\n" else False
is_in = lambda palavra, linha: True if palavra in linha else False 

def clear_spaces_no_inicio(linha):
    contador = 0
    tamanho = len(linha)
    while True:
        if contador+1 >= tamanho:
            linha = ""
            break
        if is_caracter(linha[contador]):
            break
        contador += 1
    return linha[contador:]

def registrar_classes(label):
  classes = {}
  for i in label:
    if i not in classes:
      classes[i] = 1
    elif i in classes:
      classes[i] += 1
  return classes

def separar_chave_valor(dicionario:dict):
  return list(dicionario.keys()), list(dicionario.values())

def is_linha_vazia(linha):
    formato_da_linha = [is_quebra_de_linha(c) for c in linha]
    classes = registrar_classes(formato_da_linha)
    classes, _ = separar_chave_valor(classes)

    tamanho = len(classes)
    
    if tamanho == 1 and classes[0] == True:
       return  True
    elif tamanho == 1 and classes[0] == False:
       return False
    elif tamanho > 1:
       return False

with open("Rakudai_Kishi_no_Eiyuutan_02.txt", "r", encoding="utf8") as f:
    texto = f.read()

texto = texto.replace("", "")

novo_texto = ""

texto = texto.split("\n")

# Removendo excessos de espaços
for linha in texto:
    novo_texto += f"{clear_spaces_no_inicio(linha)}\n"

novo_texto = novo_texto.split("\n")
texto = ""

# Removendo linhas vazias
for linha in novo_texto:
    if is_linha_vazia(linha) == False:
       texto += f"{linha}\n"

texto = texto.split("\n")
novo_texto = ""

# Juntando frases que terminam em virgula e foram separadas por quebra de linha.
for linha in texto:
    if len(linha) < 1:
       novo_texto += f"{linha}\n"
    elif linha[len(linha)-1] == ",":
       novo_texto += f"{linha} "
    else:
       novo_texto += f"{linha}\n"

novo_texto = novo_texto.split("\n")
texto = ""

# Juntando frases quebradas no meio.
chapter_divisors_sem_numbers = ["Rakudai Kishi no Eyuutan", "Prólogo:", "Palavras do Autor", "Epílogo:"]
chapter_divisors_com_numbers = ["Parte", "Capítulo", "Volume"]
#chapter_divisors_com_numbers = [[f"{divisor} {number}" for number in range(20)] for divisor in chapter_divisors_com_numbers]
chapter_divisors_com_numbers = [f"{divisor} {number}" for number in range(20) for divisor in chapter_divisors_com_numbers]

for linha in novo_texto:
   lista_divisors_sem_numbers = [is_in(palavra, linha) for palavra in chapter_divisors_sem_numbers]
   lista_divisors_com_numbers = [is_in(palavra, linha) for palavra in chapter_divisors_com_numbers]

   if len(linha) < 1:
      pass
   elif True in lista_divisors_sem_numbers:
      texto += f"{linha}\n"
   elif True in lista_divisors_com_numbers:
      texto += f"{linha}\n"
   else:
      if is_lower_caracter(linha[len(linha)-1]):
        texto += f"{linha} "
      elif ord(linha[len(linha)-1]) == 45:
        texto += f"{linha}"
      else:
        texto += f"{linha}\n"

with open("Resultado.txt", "w", encoding="utf8") as f:
    f.write(texto)