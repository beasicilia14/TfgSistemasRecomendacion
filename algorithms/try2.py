
from precisionRecall import getPrecisionRecall
import pandas as pd 

prec_rand, rec_rand =getPrecisionRecall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\RandomRecommendations_NewYork.txt" )

prec_pop, rec_pop = getPrecisionRecall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\PopularityRecommendationsNewYork.txt" )

prec_20, rec_20 = getPrecisionRecall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k20NewYork.txt" )

prec_30, rec_30 = getPrecisionRecall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k30NewYork.txt" )

prec_60, rec_60 = getPrecisionRecall("subsets\\NewYork_US_validation.txt","Algorithms\\Recommendations\\KNNRecommendations_k60NewYork.txt" )


data = {"K": [20, 30, 60], "Precision": [prec_20, prec_30, prec_60], "Recall": [rec_20, rec_30, rec_60]}

table = pd.DataFrame(data)

print(table)