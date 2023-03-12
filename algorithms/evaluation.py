#EVALUATE ALGORITHMS BASED ON PRECISION AND RECALL 


#PRECISION: 
#POR CADA USUARIO DE TEST, INTERSECCION ENTRE CONJUNTO POIS QUE EL USUARIO HA VISITADO EN TES
#Y CONJUNTO DE POIS QUE LE HEMOS RECOMENDADO, DIVIDIDO ENTRE NºRECOMENDACIONES

#RECALL IGUAL PERO DIVIDIMOS ENTRE Nº SITIOS TEST


#abrir validation file 
#ejecutar algoritmos para k = distintos 
#sacar todos los sitios de user validation 
#comparar 
from popularity import popularityAlgorithm
from knn import knnAlgorithm
from knn import readknn
from randomAlgorithm import randomAlgorithm
from readTrain import readTrain

pois, scores, city = readTrain("subsets/NewYork_US_train.txt")
user_poi_scores, userSquaredSum, city= readknn("subsets/NewYork_US_train.txt")

with open("subsets/NewYork_US_validation.txt") as filevalidation: 
    for line in filevalidation: 
        split_line = line.split("\t")
        user = split_line[0]
        #0: user
        #1: poi_id
        #2: timestamp 
        #3: score 

        randomAlgorithm(pois,user, 20, city)
        popularityAlgorithm(scores,pois, user, 20, city)
        knnAlgorithm(user_poi_scores,userSquaredSum,user,20,city)
        knnAlgorithm(user_poi_scores,userSquaredSum,user,30,city)
        knnAlgorithm(user_poi_scores,userSquaredSum,user,60,city)






        

