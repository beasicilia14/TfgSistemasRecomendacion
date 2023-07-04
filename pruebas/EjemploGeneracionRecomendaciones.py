from recomendador_clase import * 

#Escribir ruta del conjunto de datos que queramos utilizar para entrenar el modelo y para probarlo. 
trainset_path = "subsets/Tokyo_JP_train.txt"
testset_path = "subsets/Tokyo_JP_validation.txt"

#Escribir ruta  donde queramos guardar las recomendaciones 
recommendations_path = "pruebas//RecomendacionesTokyoFoursquare"

#Número de recomendaciones que se quieran generar para cada usuario 
numRec = 10 


#Creación de objetos
objeto_rec = Recomendador()
objeto_rand = Random()
objeto_pop = Popularity()
objeto_knn = Knn()
objeto_knnmidpoint = KnnMidpoint()
objeto_knnitem = KnnItems()
objeto_hybrid = Hybrid()

pois, scores, city = objeto_rec.readTrain(trainset_path)



#Para knn_items (Estos datos se calculan aquí para reducir el tiempo de ejecución)
user_poi_scores, city, poi_users_visited = objeto_knnitem.readknn(trainset_path)

item_similarities = objeto_knnitem.calculate_item_similarities(poi_users_visited)


#Generamos recomendaciones. 
with open(testset_path) as filetest: 
    for line in filetest: 
        split_line = line.split("\t")
        user = split_line[0]
       
        #0: user
        #1: poi_id
        #2: timestamp 

        #random
        objeto_rand.recomendar(pois,user, numRec, city, recommendations_path, trainset_path)
        
        #popularity
        objeto_pop.recomendar(pois,user, numRec, city, scores,recommendations_path, trainset_path)
        
        #knn
        objeto_knn.recomendar(trainset_path, user, numRec, 20, recommendations_path)
        

        #knn midpoint 
        objeto_knnmidpoint.recomendar(trainset_path, user, numRec, 20, recommendations_path)
       

        #hybrid 
        objeto_hybrid.recomendar(trainset_path, user, numRec, 120, recommendations_path)

        #knn item-based 

        objeto_knnitem.recomendar(user, user_poi_scores, city, item_similarities, numRec, 30, recommendations_path)


