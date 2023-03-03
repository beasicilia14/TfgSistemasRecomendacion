

#CALCULAR SCORE DE TODOS LOS PUNTOS DE INTERÉS EN TRAIN. 
#Nº Veces que un POI ha sido visitado por gente distinta 

def popularityAlgorithm(scores,pois, user, numRecom): 
    validos={}
    #scores es diccionario poi_id:score
    user_visited=pois[user]
    for i,v in scores.items(): 
        if i not in user_visited: 
            validos[i] = v
      
    pois_sorted = dict(sorted(validos.items(),key=lambda x: x[1], reverse=True))

     # Return top 30 POIs with visit counts
    pois_top30 = dict(list(pois_sorted.items())[:numRecom])

    with open("algorithms//PopularityRecommendations_user" + user + ".txt", "w") as file:
        for i, (poi, visits) in enumerate(pois_top30.items()):
            file.write(f"{i}\t{poi}\t{visits}\n")
