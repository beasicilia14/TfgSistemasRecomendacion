
import math 

def readKnnMidpoint(trainset):
    user_dicc = {}
    pois_dicc = {}

    with open(trainset) as file: 
        for line in file: 
            line_split = line.split("\t")
            #0: user_id
            #1: poi_id 
            #2: timestamp 
            #3: lon 
            #4: lat 
            #5: score 

            user_id = line_split[0]
            poi_id = line_split[1]
            lon = line_split[3]
            lat = line_split[4]

            score = line_split[5].split("\n")[0]
                
            if user_id in user_dicc.keys(): 
                user_dicc[user_id][poi_id] = int(score)
            else: 
                user_dicc[user_id] = {poi_id:int(score)}
            
            if poi_id not in pois_dicc.keys(): 
                pois_dicc[poi_id] = [lon, lat]
            else: 
                pass 
    return user_dicc, pois_dicc 


def knnMidpointCalc(user_dicc, pois_dicc): 
    dicc_midpoint = {}

    for user in user_dicc.keys(): 
        pois_visited = user_dicc[user].keys()
        x=0
        y=0
        z=0
        for poi in pois_visited: 
            lon = float(pois_dicc[poi][0])
            lat = float(pois_dicc[poi][1])
            
            lon = lon * math.pi / 180 
            lat = lat * math.pi / 180 

            x += math.cos(lat) * math.cos(lon)
            y += math.cos(lat) * math.sin(lon)
            z += math.sin(lat)

        x_weighted = x/len(pois_visited)
        y_weighted = y/len(pois_visited)
        z_weighted = z/len(pois_visited)

        lon = math.atan2(y_weighted, x_weighted)
        hyp = math.sqrt(x_weighted*x_weighted+ y_weighted*y_weighted)
        lat = math.atan2(z_weighted, hyp)

        lon = lon*180 / math.pi
        lat = lat*180 /math.pi
        dicc_midpoint[user] = [lon,lat]
    
    return dicc_midpoint 


def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia


def knnMidpointAlg (user_dicc, pois_dicc, user_test, numRec): 
    

    dicc_midpoints = knnMidpointCalc(user_dicc, pois_dicc)
    dicc_scores = {}

    #entiendo que si no está en train no le ponemos midpoint, NO SE CONSIDERA? 

    if user_test in dicc_midpoints.keys(): 
        #le puedo hacer recomendaciones 
        user_midpoint = dicc_midpoints[user_test]
        lon_midpoint = user_midpoint[0]
        lat_midpoint = user_midpoint[1]

        for i in dicc_midpoints: 
            if i != user_test: 

                midpoint_train_lon = dicc_midpoints[i][0]
                midpoint_train_lat = dicc_midpoints[i][1]

                dist = haversine(lat_midpoint, lon_midpoint, midpoint_train_lat, midpoint_train_lon)
                
                #print(dist)
                
                dicc_scores[i] = 1/dist 
    
    sorted_similarity = dict(sorted(dicc_scores.items(), key=lambda item: item[1], reverse=True))
    
    #GET K NEIGHBORS: 
    similarity_kneighbors = dict(list(sorted_similarity.items())[:numRec])

    print(similarity_kneighbors)

    dictionary_scores ={} #poi:totalscore

    for user_train in similarity_kneighbors: 
        pois_user_train = user_dicc[user_train].keys()

        weight=similarity_kneighbors[user_train]
        #print(weight)
        
        for poi in pois_user_train: 
            if poi in dictionary_scores: 
                rating = user_dicc[user_train][poi]
                dictionary_scores[poi]+= rating*weight
            else: 
                rating = user_dicc[user_train][poi]
                dictionary_scores[poi] = rating*weight 

    

    #AHORA DE TODOS LOS DISPONIBLES COJO LOS 20 PRIMEROS. 
    dictionary_scores_sorted = dict(sorted(dictionary_scores.items(), key=lambda item: item[1], reverse=True))

    pois_recommended= dict(list(dictionary_scores_sorted.items())[:numRec])

    #normalizar el score ? 


    with open("algorithms//Recommendations//especial//KNN_MIDPOINT" + str(numRec) + ".txt", "a") as file:
            index=1
            for (poi, score) in pois_recommended.items():
                file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                index+=1





