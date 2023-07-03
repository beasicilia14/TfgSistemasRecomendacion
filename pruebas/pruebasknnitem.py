
import os 

from recomendador_clase import * 

knn_object = KnnItems()

user_poi_scores, city, poi_users_visited = knn_object.readknn("merge/NewYork_USFoursquareGowalla_train.txt")



item_similarities = knn_object.calculate_item_similarities(poi_users_visited)



with open("subsets/NewYork_US_test.txt") as filetest: 
    for line in filetest: 
        split_line = line.split("\t")
        user = split_line[0]

        knn_object.recomendar(user, user_poi_scores, city, item_similarities, 10, 20, "pruebas//CarpetaProbandoTokio")

