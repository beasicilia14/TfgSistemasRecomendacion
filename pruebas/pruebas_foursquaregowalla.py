from recomendador_clase import * 

objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()

objeto_knnmidpoint = KnnMidpoint()
objeto_hybrid = Hybrid()


pois, scores, city = objeto_rec.readTrain("merge/Tokyo_JPFoursquareGowalla_train.txt")


with open("subsets/Tokyo_JP_test.txt") as filetest: 
    for line in filetest: 
        split_line = line.split("\t")
        user = split_line[0]
        #0: user
        #1: poi_id
        #2: timestamp 

        #random
        #objeto_rand.recomendar(pois,user, 10, city, "pruebas//RecomendacionesFoursquareGowallaTokyo", "merge/Tokyo_JPFoursquareGowalla_train.txt")
        
        #popularity
        #objeto_pop.recomendar(pois,user, 10, city, scores,"pruebas//RecomendacionesFoursquareGowallaTokyo", "merge/Tokyo_JPFoursquareGowalla_train.txt")
        
        #knn
        objeto_knn.recomendar("merge/Tokyo_JPFoursquareGowalla_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareGowallaTokyo")
       
        #knn midpoint 
        #
        # 
        #objeto_knnmidpoint.recomendar("merge/Tokyo_JPFoursquareGowalla_train.txt", user, 10, 120, "pruebas//RecomendacionesFoursquareGowallaTokyo")
        
        #hybrid 
        #objeto_hybrid.recomendar("merge/Tokyo_JPFoursquareGowalla_train.txt", user, 20, 30, "pruebas//RecomendacionesFoursquareGowalla")



