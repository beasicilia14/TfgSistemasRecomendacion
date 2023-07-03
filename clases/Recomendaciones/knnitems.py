import math

class KnnItems(Recomendador): 
    def readknn(self,trainset):
        user_poi_scores = {}
        userSquaredSum = {} 
        city = trainset[(trainset.index("/")+1):trainset.index("_")]
        poi_users_visited = {}

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
                    
                    #Guardo scores que los usuarios han dado a los pois, numerador. 
                    if user_id in user_poi_scores.keys(): 
                        user_poi_scores[user_id][poi] = int(score)
                    else: 
                        user_poi_scores[user_id] = {poi:int(score)}
                    

                    #Diccionario usuarios que han visitado cada poi y el score dado : {poi1: {usuario1:5 , usuario2:3}
                    if poi in poi_users_visited.keys(): 
                        poi_users_visited[poi][user_id] = int(score)
                    else: 
                        poi_users_visited[poi]= {user_id: int(score)}
                    
        
        return userSquaredSum, user_poi_scores, city, poi_users_visited


    def calculate_cosine_similarity(user_set1, user_set2):
        # Create a set containing all unique users
        
        all_users = set(user_set1 + user_set2)
        
        # Numerador
        dot_product = sum(user_set1.get(user, 0) * user_set2.get(user, 0) for user in all_users)
        
        # Calculate the magnitudes of the user sets
        magnitude1 = math.sqrt(sum(score**2 for score in user_set1.values()))
        magnitude2 = math.sqrt(sum(score**2 for score in user_set2.values()))
        
        # Denominadores igual a 0 evitar div por 0
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        # Cosine similarity
        similarity = dot_product / (magnitude1 * magnitude2)
        
        return similarity

    
    def calculate_item_similarities(self, poi_users_visited):
        item_similarities = {}
        
        for poi1, users1 in poi_users_visited.items():
            similarities = {}
            
            for poi2, users2 in poi_users_visited.items():
                if poi1 != poi2:
                    similarity = self.calculate_cosine_similarity(users1, users2)
                    similarities[poi2] = similarity
            
            item_similarities[poi1] = similarities

        item_similarities_sorted  = dict(sorted(item_similarities.items(), key=lambda item: item[1], reverse=True))
        
        return item_similarities_sorted



    def recomendar(self, user_test, user_poi_scores, city, item_similarities, numRecom,k, path_destino): 
        
        dicc_ratings = {}
        #Rating numerador --> sumatorio rui*rvi
        
        #GET POIS VISITED BY USER_TEST:
        if user_test in user_poi_scores.keys(): 
            user_visited = user_poi_scores[user_test]
        else:
            user_visited =[]

        #Recorro cada poi disponible para recomendar
        for i in user_poi_scores.keys(): 
            rating = 0 
            if i not in user_visited: 
                similarities = item_similarities[i]

                top_k_similar_pois = dict(list(similarities.items())[:k])
                
                for poi, similarity in top_k_similar_pois:
                    if poi in user_poi_scores[user_test]:  
                        weight = similarity
                        score = user_poi_scores[user_test][poi]
                        rating += weight * score 

                dicc_ratings[i] = rating 

        
        
        top_recommended_pois = dict(sorted(dicc_ratings.items(), key=lambda x: x[1], reverse=True)[:numRecom])
        
        with open(path_destino + "//KNNitems_k" + str(k) + "Recommendations" + city + ".txt", "a") as file:
                index=1
                for (poi, score) in top_recommended_pois.items():
                    file.write(f"{user_test}\t{index}\t{poi}\t{score}\n")
                    index+=1



