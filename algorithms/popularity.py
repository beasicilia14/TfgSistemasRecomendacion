

#CALCULAR SCORE DE TODOS LOS PUNTOS DE INTERÉS EN TRAIN. 
#Nº Veces que un POI ha sido visitado por gente distinta 

def popularityAlgorithm(scores,pois, user, numRecom, city): 
    validos={}
    #scores es diccionario poi_id:score
    if user in pois.keys(): 
        user_visited=pois[user]
    else: 
        user_visited = []

    for i,v in scores.items(): 
        if i not in user_visited: 
            validos[i] = v
      
    pois_sorted = dict(sorted(validos.items(),key=lambda x: x[1], reverse=True))

     # Return top 30 POIs with visit counts
    pois_top30 = dict(list(pois_sorted.items())[:numRecom])

    with open("algorithms//Recommendations//PopularityRecommendations" + city + ".txt", "a") as file:
        index=1
        for (poi, visits) in pois_top30.items():
            file.write(f"{user}\t{index}\t{poi}\t{visits}\n")
            index+=1