from popularity import popularityAlgorithm
from knn import knnAlgorithm
from knn import readknn
from randomAlgorithm import randomAlgorithm
from readTrain import readTrain


pois, scores, city = readTrain("subsets/NewYork_US_train.txt")

#RANDOM ALGORITHM: 
randomAlgorithm(pois,"264684", 20, city)
randomAlgorithm(pois,"163675", 20, city)

#POPULARITY: 
popularityAlgorithm(scores,pois, "264684", 20, city)
popularityAlgorithm(scores,pois, "163675", 20, city)

#KNN: 
user_poi_scores, userSquaredSum, city= readknn("subsets/NewYork_US_train.txt")
knnAlgorithm(user_poi_scores,userSquaredSum,"264684",20,city)
knnAlgorithm(user_poi_scores,userSquaredSum,"163675",20,city)

