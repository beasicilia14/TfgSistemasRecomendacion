from precision import precision
from recall import recall
from epc import epc
from aggregateDiversity import aggregateDiversity
import pandas as pd


def evaluate_algorithm(algorithm_path, validation_data_path, train_data_path, k):
    prec = precision(algorithm_path, validation_data_path, k)
    rec = recall(algorithm_path, validation_data_path, k)
    epc_val = epc(algorithm_path, train_data_path, k)
    agg_div = aggregateDiversity(algorithm_path, k)
    return prec, rec, epc_val, agg_div


algorithm_paths = [
    "algorithms\\Recommendations\\RandomRecommendationsNewYork.txt",
    "algorithms\\Recommendations\\PopularityRecommendationsNewYork.txt",
    "algorithms\\Recommendations\\KNNRecommendations_K20NewYork.txt",
    "algorithms\\Recommendations\\KNNRecommendations_K30NewYork.txt",
    "algorithms\\Recommendations\\KNNRecommendations_K60NewYork.txt",
]

validation_data_path = "subsets\\NewYork_US_validation.txt"
train_data_path = "subsets/NewYork_US_train.txt"
k = 10

algorithm_names = ["Random", "Popularity", "K20", "K30", "K60"]

data = {"Algorithm": [], "Precision": [], "Recall": [], "epc": [], "AggDiversity": []}

for i, algorithm_path in enumerate(algorithm_paths):
    prec, rec, epc_val, agg_div = evaluate_algorithm(algorithm_path, validation_data_path, train_data_path, k)
    data["Algorithm"].append(algorithm_names[i])
    data["Precision"].append(prec)
    data["Recall"].append(rec)
    data["epc"].append(epc_val)
    data["AggDiversity"].append(agg_div)

table = pd.DataFrame(data)

print(table)
