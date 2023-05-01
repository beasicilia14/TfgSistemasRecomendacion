from recomendador_clase import * 

objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()

objeto_knnmidpoint = KnnMidpoint()
objeto_hybrid = Hybrid()


pois, scores, city = objeto_rec.readTrain("subsets/NewYork_US_train.txt")


with open("subsets/NewYork_US_validation.txt") as filevalidation: 
    for line in filevalidation: 
        split_line = line.split("\t")
        user = split_line[0]
        #0: user
        #1: poi_id
        #2: timestamp 

        #random
        objeto_rand.recomendar(pois,user, 20, city, "pruebas//RecomendacionesFoursquare", "subsets/NewYork_US_train.txt")
        
        #popularity
        objeto_pop.recomendar(pois,user, 20, city, scores,"pruebas//RecomendacionesFoursquare", "subsets/NewYork_US_train.txt")
        
        #knn
        objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 20, 30, "pruebas//RecomendacionesFoursquare")
       
        #knn midpoint 
        objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 20, 30, "pruebas//RecomendacionesFoursquare")
        
        #hybrid 
        objeto_hybrid.recomendar("subsets/NewYork_US_train.txt", user, 20, 30, "pruebas//RecomendacionesFoursquare")



