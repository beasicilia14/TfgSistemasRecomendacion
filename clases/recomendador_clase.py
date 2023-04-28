import random
import math 
from funciones import * 

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
        file_name = path_destino + "//RandomRecom" + city + ".txt"
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


    def recomendar(self, trainset, user_test,numRecom,k, path_destino): 
        
        userSquaredSum, user_poi_scores, city = self.readknn(trainset)
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
        similarity_kneighbors = dict(list(sorted_similarity.items())[:k])

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

        with open(path_destino + "//KNNRecommendations_k" + str(k) + city + ".txt", "a") as file:
                index=1
                for (poi, score) in pois_recommended.items():
                    file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                    index+=1


class KnnMidpoint(Recomendador):
    
    def readKnnMidpoint(self, trainset):
        user_dicc = {}
        pois_dicc = {}
        city = trainset[(trainset.index("/")+1):trainset.index("_")]

        with open(trainset) as file: 
            for line in file: 
                line_split = line.split("\t")
                #0: user_id
                #1: poi_id 
                #2: timestamp 
                #3: lat 
                #4: lon
                #5: score 

                user_id = line_split[0]
                poi_id = line_split[1]
                lat = line_split[3]
                lon = line_split[4]
                score = line_split[5].split("\n")[0]
                
                #dicc user: poi1, poi2, 
                if user_id in user_dicc.keys(): 
                    user_dicc[user_id][poi_id] = int(score)
                else: 
                    user_dicc[user_id] = {poi_id:int(score)}
                
                #dicc poi: lat lon 
                if poi_id not in pois_dicc.keys(): 
                    pois_dicc[poi_id] = [lat, lon]
                else: 
                    pass 
        return user_dicc, pois_dicc , city


    def knnMidpointCalc(self, user_dicc, pois_dicc): 
        dicc_midpoint = {}

        for user in user_dicc.keys(): 
            pois_visited = user_dicc[user].keys()
            x=0
            y=0
            z=0
            for poi in pois_visited: 
                lat= float(pois_dicc[poi][0])
                lon = float(pois_dicc[poi][1])
                
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

            #midpoint de cada usuario que está en train 
            dicc_midpoint[user] = [lat,lon]
        
        return dicc_midpoint 


    
    def recomendar(self, trainset, user_test, numRec, k, path): 
        
        user_dicc, pois_dicc , city= self.readKnnMidpoint(trainset)

        #user dicc: usuarios & pois 
        #pois dicc : pois: lon, lat 

        dicc_midpoints = self.knnMidpointCalc(user_dicc, pois_dicc)

        dicc_scores = {}

        #entiendo que si no está en train no le ponemos midpoint, NO SE CONSIDERA? 

        if user_test in dicc_midpoints.keys(): 
            #le puedo hacer recomendaciones 
            user_midpoint = dicc_midpoints[user_test]
            lat_midpoint = user_midpoint[0]
            lon_midpoint = user_midpoint[1]

            #comparo con todos los midpoints de los users de train
            for i in dicc_midpoints: 
                if i != user_test: 

                    midpoint_train_lat = dicc_midpoints[i][0]
                    midpoint_train_lon = dicc_midpoints[i][1]

                    dist = haversine(lat_midpoint, lon_midpoint, midpoint_train_lat, midpoint_train_lon)
                    
                    if dist==0: 
                        dist = 0.001 
                        dicc_scores[i] = 1/dist 
                    else: 
                        dicc_scores[i] = 1/dist 
                    #print(dist)
                    
                    
        #ordenamos según los que tengan mayor relación 
        sorted_similarity = dict(sorted(dicc_scores.items(), key=lambda item: item[1], reverse=True))
        
        #GET K NEIGHBORS: 
        similarity_kneighbors = dict(list(sorted_similarity.items())[:k])

        #print(similarity_kneighbors)

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

        

        #AHORA DE TODOS LOS DISPONIBLES CON SUS SCORES COJO LOS 20 PRIMEROS. 
        dictionary_scores_sorted = dict(sorted(dictionary_scores.items(), key=lambda item: item[1], reverse=True))

        pois_recommended= dict(list(dictionary_scores_sorted.items())[:numRec])




        with open(path + "//KNN_MidpointRecommendations_k" + str(k) + city + ".txt", "a") as file:
                index=1
                for (poi, score) in pois_recommended.items():
                    file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                    index+=1


    def reRanking(self, trainset, user_test, recomendaciones, path): 
        user_dicc, pois_dicc , city= self.readKnnMidpoint(trainset)

        #user dicc: usuarios & pois 
        #pois dicc : pois: lon, lat 
        dicc_filtrado={}
        #quiero solo el midpoint del de test 
        dicc_filtrado[user_test]= user_dicc[user_test]

        dicc_midpoints = self.knnMidpointCalc(dicc_filtrado, pois_dicc)

        dicc_scores = {}

        #entiendo que si no está en train no le ponemos midpoint, NO SE CONSIDERA? 

        if user_test in dicc_midpoints.keys(): 
            #le puedo hacer recomendaciones 
            user_midpoint = dicc_midpoints[user_test]
            lat_midpoint = user_midpoint[0]
            lon_midpoint = user_midpoint[1]

            #comparo con todos los midpoints de los users de train
            for i in recomendaciones: 
                recom_lat = pois_dicc[i][0]
                recom_lon = pois_dicc[i][1]

                dist = haversine(lat_midpoint, lon_midpoint, recom_lat, recom_lon)

                if dist==0: 
                    dist = 0.001 
                    dicc_scores[i] = 1/dist
                else: 
                    dicc_scores[i] = 1/dist
            

                        #print(dist)

        #ordenamos según los que tengan mayor relación 
            sorted_similarity = dict(sorted(dicc_scores.items(), key=lambda item: item[1], reverse=True))
            
            with open(path + "//MidpointRerankedRecommendations" + city + ".txt", "a") as file:
                index=1
                for (poi, score) in sorted_similarity.items():
                    file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                    index+=1



class Hybrid(Recomendador): 
  
    
    def recomendar(self, trainset, user_test, numRec, k, path): 
        objeto_pop = Popularity()
        objeto_knn = Knn()
        objeto_knnmidpoint = KnnMidpoint()
        pois, scores, city = objeto_pop.readTrain("subsets/NewYork_US_train.txt")

        #pillando las rec hechas antes o ?
        #
        
        path_temp = "clases//intermediate"
        objeto_pop.recomendar(pois,user_test, 20, city, scores,path_temp)
        objeto_knn.recomendar(trainset, user_test, numRec, k,  path_temp)
        objeto_knnmidpoint.recomendar(trainset, user_test, numRec, k,  path_temp)

        file_rec_pop = path_temp + "//PopularityRecommendations" + city + ".txt"

        file_rec_knn = path_temp + "//KNNRecommendations_k" + str(k) + city + ".txt"

        file_rec_midpoint = path_temp + "//KNN_MidpointRecommendations_k" + str(k) + city + ".txt"


        dicc_pop = {}
        dicc_knn ={}
        dicc_mid = {}

        with open(file_rec_pop) as file_pop: 
            for line in file_pop: 
                line_split = line.split("\t")
                poi_id = line_split[2]
                score = line_split[3].split("\n")[0]

                dicc_pop[poi_id]= float(score)
            
        file_pop.close()
        with open(file_rec_pop, 'w') as file_pop:
            file_pop.write('')
        
        with open(file_rec_knn) as file_knn: 
            for line in file_knn: 
                line_split = line.split("\t")
                poi_id = line_split[2]
                score = line_split[3].split("\n")[0]
                dicc_knn[poi_id]= float(score)
            
        file_knn.close()
        with open(file_rec_knn, 'w') as file_knn:
            file_knn.write('')
        
        with open(file_rec_midpoint) as file_mid: 
            for line in file_mid: 
                line_split = line.split("\t")
                poi_id = line_split[2]
                score = line_split[3].split("\n")[0]
                dicc_mid[poi_id]= float(score)
       
        file_mid.close()
        with open(file_rec_midpoint, 'w') as file_mid:
            file_mid.write('')
        
        dicc_pop= normalizeDicc(dicc_pop)

        if dicc_knn != {}: 
            dicc_knn = normalizeDicc(dicc_knn)
        
        if dicc_mid != {}: 
            dicc_mid = normalizeDicc(dicc_mid)

        
        dicc_total = {}

        for i in dicc_pop: 
            dicc_total[i] = dicc_pop[i]

        if dicc_knn != {}:
            for i in dicc_knn: 
                if i in dicc_total: 
                    dicc_total[i] += dicc_knn[i]
                else: 
                    dicc_total[i] = dicc_knn[i]
        
        if dicc_mid !={}:
            for i in dicc_mid: 
                if i in dicc_total: 
                    dicc_total[i] += dicc_mid[i]
                else: 
                    dicc_total[i] = dicc_mid[i]

        #cogemos top 20 pois según score 
        
    #AHORA DE TODOS LOS DISPONIBLES COJO LOS 20 PRIMEROS. 
        dictionary_top20 = dict(sorted(dicc_total.items(), key=lambda item: item[1], reverse=True))

        pois_recommended= dict(list(dictionary_top20.items())[:numRec])


        with open(path + "//HybridRecommendation" + city + ".txt", "a") as file:
                index=1
                for (poi, score) in pois_recommended.items():
                    file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                    index+=1

        #(self, trainset, user_test, numRec, k, path)
        # def readKnnMidpoint(self, trainset)
        # def knnMidpointCalc(self, user_dicc, pois_dicc)




