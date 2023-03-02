
#Para cada usuario de test, recomendará puntos de interés aleatorios entre todos los que están en 
#validación y train que el usuario no haya visitado en ninguno de los conjuntos. 

import random

def readTrainSet(validationset, trainset, user, numRecom):
    pois = {}

    # Add POIs from testset that user has not visited
    with open(trainset) as train:
        for line in train:
            split_line =line.split("\t")
            user_id=split_line[0]
            venue_id =split_line[1]

            #check para no recomendar POI que el user ya haya ido
            #if user_id != user:
            if user_id not in pois.keys(): 
                pois[user_id] = [venue_id]
            else:
                pois[user_id].append(venue_id)
                
    # Add POIs from validationset that user has not visited
    with open(validationset) as validation:
        for line in validation:
            split_line =line.split("\t")
            user_id=split_line[0]
            venue_id =split_line[1]

            if user_id not in pois.keys(): 
                pois[user_id] = [venue_id]
            else:
                pois[user_id].append(venue_id)

    return pois

#devuelve user:poi1, poi2, poi3

def randomAlgorithm(pois,user, numRecom): 

    validos = set()
    for k,v in pois.items(): 
        if k != user: 
            for i in v: 
                validos.add(int(i))
 
    pois_list = list(validos)
    random_items = random.sample(pois_list, numRecom)
    #random.shuffle(pois_list)
    # Return first n POIs
    file_name = "algorithms//RandomRecommendations_user" + user + ".txt"
    file = open(file_name, 'w')
    ind=0
    
    for i in random_items:
        file.write(str(ind)+ "\t" + str(i) + "\n")
        ind+=1



