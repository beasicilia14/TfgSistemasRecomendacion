
#CALCULATE SIMILARITY: 

#algorithm calculates rating between users. 
#approach: 
#1)Create a dictionary that has: user: {poi:score, poi2:score}
#2) Get pois that user has visited 
#3) if usertrain1 has visited any places == usertest its rating will improve. 

#dictionary to store: --> user:{poi1:score1, poi2:score2....}
#num: only comunes 
#den: todos y al cuadrado 



import math 



def knnAlgorithm(trainset, user_test): 
        
    user_poi_scores = {}
    userSquaredSum = {} #poner sumatorio de score al cuadrado de cada uno 
    similarity_scores  ={}

    with open(trainset) as train:
            for line in train:
                split_line =line.split("\t")
                #0: user
                #1: poi
                #2: timestamp
                #3: score 
                user_id=split_line[0]
                poi =split_line[1]
                score = split_line[3]
                

                if user_id in user_poi_scores.keys(): 
                    user_poi_scores[user_id][poi] = int(score)
                else: 
                    user_poi_scores[user_id] = {int(poi):int(score)}

                #para denominador. 
                if int(user_id) not in userSquaredSum:
                    userSquaredSum[int(user_id)] = int(score.strip())**2
                else:
                    userSquaredSum[int(user_id)] += int(score.strip())**2


    #Rating numerador --> sumatorio rui*rvi

    #GET POIS VISITED BY USER_TEST:
    if user_test in user_poi_scores.keys(): 
        user_visited = user_poi_scores[user_test]
    else:
        user_visited =[]


    #CALCULANDO SIMILITUD CON CADA UNO DE LOS USUARIOS. 

    for user_train in user_poi_scores: 
        
        if user_train != user_test: 
        
            numerador =0 
            for poi in user_visited: 
                pois_train= user_poi_scores[user_train]

                if poi in pois_train: 
                    numerador+= user_poi_scores[user_train][poi] * user_poi_scores[user_test][poi]
            
            #condition is necessary to ensure that both users have rated at least one POI
            #and their sum of squares is not zero, before computing the similarity between them.
            if int(user_train) in userSquaredSum and int(user_test) in userSquaredSum: 
                
                denominador = math.sqrt(userSquaredSum[int(user_train)] * userSquaredSum[int(user_test)])
                
                
            
                if numerador !=0: 
                    similarity_scores[user_train]= numerador/denominador

    #USERS WITH HIGHEST SIMILARITY. 
    sorted_similarity = dict(sorted(similarity_scores.items(), key=lambda item: item[1], reverse=True))

    #GET K NEIGHBORS: 
    similarity_30neighbors = dict(list(sorted_similarity.items())[:30])

    #Ahora hay que calcular el rui (u=usuario test, i=poi)
    #rui = sum w_uv * r_vi
    #niu es users who have rated item i . 
    #get all users that have rated x 
    #get for each user, w and r 
    #Add to sum. 

    #diccionario que sea poi_id: rating 
    #if poi_id in diccionario, sumo rating de ese usuario. 
    dictionary_scores ={} #poi:totalscore

    for user_train in similarity_30neighbors: 
        pois_user_train = user_poi_scores[user_train]
        weight=similarity_30neighbors[user_train]
        
        for poi in pois_user_train: 
            if poi in dictionary_scores: 
                
                rating = user_poi_scores[user_train][poi]
                dictionary_scores[poi]+= rating*weight
            else: 
                rating = user_poi_scores[user_train][poi]
                dictionary_scores[poi] = rating*weight 



    #AHORA DE TODOS LOS DISPONIBLES COJO LOS 20 PRIMEROS. 
    dictionary_scores_sorted = dict(sorted(dictionary_scores.items(), key=lambda item: item[1], reverse=True))

    pois_recommended= dict(list(dictionary_scores_sorted.items())[:30])

    
    return pois_recommended












