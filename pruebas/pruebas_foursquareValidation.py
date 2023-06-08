from recomendador_clase import * 

objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()

objeto_knnmidpoint = KnnMidpoint()
objeto_hybrid = Hybrid()


pois, scores, city = objeto_rec.readTrain("subsets/Tokyo_JP_train.txt")


with open("subsets/Tokyo_JP_validation.txt") as filevalidation: 
    for line in filevalidation: 
        split_line = line.split("\t")
        user = split_line[0]
        #0: user
        #1: poi_id
        #2: timestamp 

        #random
        #objeto_rand.recomendar(pois,user, 10, city, "pruebas//RecomendacionesFoursquareValidation", "subsets/NewYork_US_train.txt")
        
        #popularity
        #objeto_pop.recomendar(pois,user, 10, city, scores,"pruebas//RecomendacionesFoursquareValidation", "subsets/NewYork_US_train.txt")
        
        #knn
        objeto_knn.recomendar("subsets/Tokyo_JP_train.txt", user, 10, 20, "pruebas//RecomendacionesFoursquareValidationTokyo")
        objeto_knn.recomendar("subsets/Tokyo_JP_train.txt", user, 10, 30, "pruebas//RecomendacionesFoursquareValidationTokyo")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 40, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 50, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 60, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 100, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareValidation")


       
        #knn midpoint 
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 20, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 30, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 40, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 50, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 60, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 100, "pruebas//RecomendacionesFoursquareValidation")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareValidation")

        #hybrid 
        #objeto_hybrid.recomendar("subsets/NewYork_US_train.txt", user, 12, 30, "pruebas//RecomendacionesFoursquareValidation")



