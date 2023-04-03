from recomendador_clase import * 

objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()

pois, scores, city = objeto_rec.readTrain("subsets/NewYork_US_train.txt")


userSquaredSum, user_poi_scores, city= objeto_knn.readknn("subsets/NewYork_US_train.txt")


#random
objeto_rand.recomendar(pois,"187542", 20, city, "Recomendaciones")
#popularity
objeto_pop.recomendar(pois,"187542", 20, city, scores,"Recomendaciones")
#knn
objeto_knn.recomendar(userSquaredSum, user_poi_scores, "187542", 20, city, "Recomendaciones")

