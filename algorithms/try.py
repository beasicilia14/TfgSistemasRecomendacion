from popularity import popularityAlgorithm
from knn import knnAlgorithm
from knn import readknn
from randomAlgorithm import randomAlgorithm
from readTrain import readTrain


pois, scores = readTrain("subsets/NewYork_US_train.txt")

#RANDOM ALGORITHM: 
randomAlgorithm(pois,"264684", 20)

#POPULARITY: 
popularityAlgorithm(scores,pois, "264684", 20)

#KNN: 
user_poi_scores, userSquaredSum = readknn("subsets/NewYork_US_train.txt")
knnAlgorithm(user_poi_scores,userSquaredSum,"264684",20)
