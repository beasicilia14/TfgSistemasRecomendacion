from aggregateDiversity import aggregateDiversity
from epc import epc

a= aggregateDiversity("algorithms\\Recommendations\\PopularityRecommendationsNewYork.txt", 5)
b= aggregateDiversity("algorithms\\Recommendations\\RandomRecommendationsNewYork.txt", 5)

c= epc("algorithms\\Recommendations\\PopularityRecommendationsNewYork.txt","subsets//NewYork_US_train.txt", 5)
d= epc("algorithms\\Recommendations\\RandomRecommendationsNewYork.txt","subsets//NewYork_US_train.txt", 5)

print("epc popularity", c)
print("epc random",  d)

print("aggregate diversity popularity", a)
print("aggregate diversity random",  b)