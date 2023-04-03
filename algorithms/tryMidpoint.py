from knn_midpoint import readKnnMidpoint
from knn_midpoint import knnMidpointCalc
from knn_midpoint import knnMidpointAlg

user_dicc, pois_dicc = readKnnMidpoint("subsets\\NewYork_US_train.txt")

with open("subsets/NewYork_US_validation.txt") as filevalidation: 
    for line in filevalidation: 
        line_split = line.split("\t")
        user = line_split[0]
        knnMidpointAlg (user_dicc, pois_dicc, user, 5)