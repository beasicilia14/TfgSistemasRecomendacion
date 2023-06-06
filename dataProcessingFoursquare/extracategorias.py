



dicc_categorias = {}

with open("dataProcessingFoursquare//intermediateFiles//NewYork_USFiltered.txt") as filenyc: 
    for line in filenyc: 
        line_split = line.split("\t")
        categoria = line_split[2]

        if categoria in dicc_categorias.keys(): 
            dicc_categorias[categoria] += 1
        else: 
            dicc_categorias[categoria] = 1

# Ordenar el diccionario de mayor a menor según los valores
dicc_categorias_ordenado = dict(sorted(dicc_categorias.items(), key=lambda x: x[1], reverse=True))


