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
        objeto_rand.recomendar(pois,user, 20, city, "clases//Recomendaciones")
        #popularity
        objeto_pop.recomendar(pois,user, 20, city, scores,"clases//Recomendaciones")
        #knn
        objeto_knn.recomendar("subsets/NewYork_US_train.txt", user, 20, "clases//Recomendaciones")
        #knn midpoint 
        objeto_knnmidpoint.recomendar("subsets/NewYork_US_train.txt", user, 20, "clases//Recomendaciones")
        #hybrid 
        #objeto_hybrid.recomendar("subsets/NewYork_US_train.txt", user, 20, "clases//Recomendaciones")



