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
        line_split = line.split("\t")
        user = line_split[0]

        knnAlgorithm(user_poi_scores,userSquaredSum,"187542",20,city)