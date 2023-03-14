
#Para cada usuario de test, recomendará puntos de interés aleatorios entre todos los que están en 
#validación y train que el usuario no haya visitado en ninguno de los conjuntos. 

import random


#devuelve user:poi1, poi2, poi3

def randomAlgorithm(pois,user, numRecom,city): 

    validos = set()
    for k,v in pois.items(): 
        if k != user: 
            for i in v: 
                validos.add(int(i))
 
    pois_list = list(validos)
    random_items = random.sample(pois_list, numRecom)
    #random.shuffle(pois_list)
    # Return first n POIs
    file_name = "algorithms//Recommendations//RandomRecommendations" + city + ".txt"
    file = open(file_name, 'a')
    ind=1
    
    for i in random_items:
        file.write(str(user)+ "\t" + str(ind)+ "\t" + str(i) + "\n")
        ind+=1



