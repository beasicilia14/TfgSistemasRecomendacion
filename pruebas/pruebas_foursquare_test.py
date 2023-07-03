from recomendador_clase import * 

objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()

objeto_knnmidpoint = KnnMidpoint()
objeto_hybrid = Hybrid()


pois, scores, city = objeto_rec.readTrain("subsets/Tokyo_JP_train_completo.txt")


with open("subsets/Tokyo_JP_test.txt") as filetest: 
    for line in filetest: 
        split_line = line.split("\t")
        user = split_line[0]
        #0: user
        #1: poi_id
        #2: timestamp 

        #random
        #objeto_rand.recomendar(pois,user, 10, city, "pruebas//RecomendacionesFoursquareTestTokyo", "subsets/Tokyo_JP_train_completo.txt")
        
        #popularity
        #objeto_pop.recomendar(pois,user, 10, city, scores,"pruebas//RecomendacionesFoursquareTestTokyo", "subsets/Tokyo_JP_train_completo.txt")
        
        #knn
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 20, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 30, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 40, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 50, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 60, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 100, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knn.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareTestTokyo")


       
        #knn midpoint 
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 20, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 30, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 40, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 50, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 60, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 100, "pruebas//RecomendacionesFoursquareTest")
        #objeto_knnmidpoint.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareTestTokyo")

        #hybrid 
        objeto_hybrid.recomendar("subsets/Tokyo_JP_train_completo.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareTestTokyo")



