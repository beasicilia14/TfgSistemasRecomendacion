from recomendador_clase import * 

objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()

objeto_knnmidpoint = KnnMidpoint()
objeto_hybrid = Hybrid()


pois, scores, city = objeto_rec.readTrain("subsets/NewYork_US_train.txt")


with open("subsets/NewYork_US_test.txt") as filetest: 
    for line in filetest: 
        split_line = line.split("\t")
        user = split_line[0]
        #0: user
        #1: poi_id
        #2: timestamp 

        #random
        #objeto_rand.recomendar(pois,user, 10, city, "pruebas//RecomendacionesFoursquareTest", "subsets/NewYork_US_train.txt")
        
        #popularity
        #objeto_pop.recomendar(pois,user, 10, city, scores,"pruebas//RecomendacionesFoursquareTest", "subsets/NewYork_US_train.txt")
        
        #knn
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 20, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 30, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 40, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 50, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 60, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 100, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareTest")


       
        #knn midpoint 
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 20, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 30, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 40, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 50, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 60, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 100, "pruebas//RecomendacionesFoursquareTest")
        objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareTest")

        #hybrid 
        #objeto_hybrid.recomendar("subsets/NewYork_US_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareTest")



