import random
import math 

class Recomendador: 

    def readTrain(self,trainset):
        pois ={}
        scores={}

        city = trainset[(trainset.index("/")+1):trainset.index("_")]

        with open(trainset) as file2:
            for line in file2:
                split_line =line.split("\t")
                user_id=int(split_line[0])
                venue_id =int(split_line[1])

                if user_id not in pois.keys(): 
                    pois[user_id] = set([venue_id])
                else:
                    pois[user_id].add(venue_id)

                if venue_id in scores.keys(): 
                    scores[venue_id] += 1
                else:
                    scores[venue_id] =1

        return pois, scores , city
    
    def recomendar(self, lista_pois, usuario, numeroRecomendaciones, city, path_destino): 
        pass 



class Random(Recomendador):
    def recomendar(self, lista_pois, usuario, numeroRecomendaciones, city, path_destino): 
        validos = set()
        for k,v in lista_pois.items(): 
            if k != usuario: 
                for i in v: 
                    validos.add(int(i))
    
        pois_list = list(validos)
        random_items = random.sample(pois_list, numeroRecomendaciones)
        #random.shuffle(pois_list)
        # Return first n POIs
        file_name = path_destino + "\\RandomRecom" + city + ".txt"
        file = open(file_name, 'a')
        ind=1
        
        for i in random_items:
            file.write(str(usuario)+ "\t" + str(ind)+ "\t" + str(i) + "\n")
            ind+=1


class Popularity(Recomendador): 
        def recomendar(self, lista_pois, usuario, numeroRecomendaciones, city, scores, path_destino): 
            validos={}
            #scores es diccionario poi_id:score
            if usuario in lista_pois.keys(): 
                user_visited=lista_pois[usuario]
            else: 
                user_visited = []

            for i,v in scores.items(): 
                if i not in user_visited: 
                    validos[i] = v
            
            pois_sorted = dict(sorted(validos.items(),key=lambda x: x[1], reverse=True))

            # Return top 30 POIs with visit counts
            pois_top30 = dict(list(pois_sorted.items())[:numeroRecomendaciones])

            with open(path_destino + "//PopularityRecommendations" + city + ".txt", "a") as file:
                index=1
                for (poi, visits) in pois_top30.items():
                    file.write(f"{usuario}\t{index}\t{poi}\t{visits}\n")
                    index+=1


class Knn(Recomendador): 
    def readknn(self,trainset):
        user_poi_scores = {}
        userSquaredSum = {} 
        city = trainset[(trainset.index("/")+1):trainset.index("_")]

        with open(trainset) as train:
                for line in train:
                    split_line =line.split("\t")
                    #0: user
                    #1: poi
                    #2: timestamp
                    #5: score 
                    user_id=split_line[0]
                    poi =split_line[1]
                    score = split_line[5].split("\n")[0]
                    

                    if user_id in user_poi_scores.keys(): 
                        user_poi_scores[user_id][poi] = int(score)
                    else: 
                        user_poi_scores[user_id] = {poi:int(score)}

                    #para denominador. 
                    if user_id not in userSquaredSum:
                        userSquaredSum[user_id] = int(score.strip())**2
                    else:
                        userSquaredSum[user_id] += int(score.strip())**2
        
        return userSquaredSum, user_poi_scores, city


    def recomendar(self, userSquaredSum, user_poi_scores, user_test,numRecom,city, path_destino): 
        
        similarity_scores  ={}

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
                if user_train in userSquaredSum and user_test in userSquaredSum: 
                    
                    denominador = math.sqrt(userSquaredSum[user_train] * userSquaredSum[user_test])
                    
                    
                
                    if numerador !=0: 
                        similarity_scores[user_train]= numerador/denominador

        #USERS WITH HIGHEST SIMILARITY. 
        sorted_similarity = dict(sorted(similarity_scores.items(), key=lambda item: item[1], reverse=True))

        #GET K NEIGHBORS: 
        similarity_kneighbors = dict(list(sorted_similarity.items())[:numRecom])

        #Ahora hay que calcular el rui (u=usuario test, i=poi)
        #rui = sum w_uv * r_vi
        #niu es users who have rated item i . 
        #get all users that have rated x 
        #get for each user, w and r 
        #Add to sum. 

        #diccionario que sea poi_id: rating 
        #if poi_id in diccionario, sumo rating de ese usuario. 
        dictionary_scores ={} #poi:totalscore

        for user_train in similarity_kneighbors: 
            pois_user_train = user_poi_scores[user_train]
            weight=similarity_kneighbors[user_train]
            
            for poi in pois_user_train: 
                if poi in dictionary_scores: 
                    
                    rating = user_poi_scores[user_train][poi]
                    dictionary_scores[poi]+= rating*weight
                else: 
                    rating = user_poi_scores[user_train][poi]
                    dictionary_scores[poi] = rating*weight 

        

        #AHORA DE TODOS LOS DISPONIBLES COJO LOS 20 PRIMEROS. 
        dictionary_scores_sorted = dict(sorted(dictionary_scores.items(), key=lambda item: item[1], reverse=True))

        pois_recommended= dict(list(dictionary_scores_sorted.items())[:numRecom])

        with open(path_destino + "//KNNRecommendations_k" + str(numRecom) + city + ".txt", "a") as file:
                index=1
                for (poi, score) in pois_recommended.items():
                    file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                    index+=1
