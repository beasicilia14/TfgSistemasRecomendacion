
from precision import precision
from recall import recall 

import pandas as pd 

prec_rand=precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\RandomRecommendationsNewYork.txt", 10)
rec_rand=recall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\RandomRecommendationsNewYork.txt" , 10)

prec_pop= precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\PopularityRecommendationsNewYork.txt", 10 )
rec_pop= recall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\PopularityRecommendationsNewYork.txt", 10 )

prec_20= precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k20NewYork.txt" , 10)
rec_20= precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k20NewYork.txt" , 10)

prec_30= precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k30NewYork.txt", 10 )
rec_30= precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k30NewYork.txt", 10 )

prec_60= precision("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k60NewYork.txt" , 10)
rec_60= recall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k60NewYork.txt" , 10)


data = {"Algorithm": ["Random", "Popularity", "K20", "k30", "k60"], "Precision": [prec_rand, prec_pop, prec_20, prec_30, prec_60], "Recall": [rec_rand, rec_pop, rec_20, rec_30, rec_60]}

table = pd.DataFrame(data)

print(table)