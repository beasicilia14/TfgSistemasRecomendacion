

#CALCULAR SCORE DE TODOS LOS PUNTOS DE INTERÉS EN TRAIN. 
#Nº Veces que un POI ha sido visitado por gente distinta 

def popularityAlgorithm(validationset,trainset,user):
    # Dictionary of POIs with visit counts

    pois ={}

    # Calculating score (visit counts)
    with open(trainset) as train:
        for line in train:
            split_line =line.split("\t")
            user_id=split_line[0]
            venue_id =split_line[1]

            #check para no recomendar POI que el user ya haya ido
            if user_id !=user:
                if venue_id in pois.keys(): 
                    pois[venue_id] += 1
                else:
                    pois[venue_id] =1
                
            
    # Add POIs from validationset that user has not visited
    with open(validationset) as validation:
            for line in validation:
                split_line =line.split("\t")
                user_id=split_line[0]
                venue_id =split_line[1]
                
                if user_id != user:
                #check para no recomendar POI que el user ya haya ido
                    if venue_id in pois.keys(): 
                        pois[venue_id] += 1
                    else:
                        pois[venue_id] =1
    
    pois_sorted = dict(sorted(pois.items(),key=lambda x: x[1], reverse=True))

     # Return top 30 POIs with visit counts
    pois_top30 = dict(list(pois_sorted.items())[:30])

    with open("algorithms//PopularityRecommendations_user" + user + ".txt", "w") as f:
        for i, (poi, visits) in enumerate(pois_top30.items()):
            f.write(f"{i}\t{poi}\t{visits}\n")

