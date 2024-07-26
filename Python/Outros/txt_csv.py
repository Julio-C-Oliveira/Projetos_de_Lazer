def txt_excel(arquivo, divisor):
    with open(arquivo, "r") as f:
        file = f.read()

    data = []
    selection = lambda x: True if ("MSE:" in x) or ("Pearson:" in x) else False
    file = file.split("\n")

    for row in file:
        if selection(row) == True:
            data.append(row)

    def separar_MSE_Pearson(row):
        row = row.replace("MSE: ", "")
        row = row.replace("Pearson: ", "")
        return float(row)

    MSEs = []
    pearsonS = []
    mudar_estado = lambda estado: True if estado == False else False
    estado = True

    for x in data:
        row = separar_MSE_Pearson(x)
        if estado == True:
            MSEs.append(row)
        else:
            pearsonS.append(row)
        estado = mudar_estado(estado)

    # print(f"MSE: {len(MSEs)} | Pearson: {len(pearsonS)}")

    selected_MSE = []
    selected_Pearsons = []

    for i in range(len(MSEs)):
        if (i+1) % divisor == 0:
            selected_MSE.append(MSEs[i])

    for i in range(len(pearsonS)):
        if (i+1) % divisor == 0:
            selected_Pearsons.append(pearsonS[i])

    # print(len(selected_MSE))
    # print(len(selected_Pearsons))

    return [selected_MSE, selected_Pearsons]

arquivos = [("random_tree.txt", 5), ("best_trees.txt", 5), ("threshold.txt", 3), ("best_forests.txt", 5)]

resultados = []

for arquivo in arquivos:
    resultados.append(txt_excel(arquivo[0], arquivo[1]))

print(f"MSEs: {len(resultados[0][0])} | {len(resultados[1][0])} | {len(resultados[2][0])} | {len(resultados[3][0])}")
print(f"Pearsons: {len(resultados[0][1])} | {len(resultados[1][1])} | {len(resultados[2][1])} | {len(resultados[3][1])}")

file_name = "SOX.csv"

csv_file = ""

csv_file += "MSE Random_Tree,MSE Best_Trees,MSE Threshold,MSE Best_Forests,Pearson Random_Tree,Pearson Best_Trees,Pearson Threshold,Pearson Best_Forests\n"

for i in range(len(resultados[0][0])):
  csv_file += f"{resultados[0][0][i]}, {resultados[1][0][i]}, {resultados[2][0][i]}, {resultados[3][0][i]}, {resultados[0][1][i]}, {resultados[1][1][i]}, {resultados[2][1][i]}, {resultados[3][1][i]}\n"

with open(file_name, "w") as f:
  f.write(csv_file)