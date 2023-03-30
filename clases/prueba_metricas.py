from metrica_clase import * 

import pandas as pd 

def evaluate_algorithm(rec_path, validation_data_path, train_data_path, k):
    object_metrica = Metrica(rec_path, validation_data_path,train_data_path,k)
    prec = object_metrica.precision()
    rec = object_metrica.recall()
    epc = object_metrica.epc()
    agg = object_metrica.aggregateDiversity()
    
    return prec, rec, epc, agg 

rec_paths = [
    "clases\\Recomendaciones\\RandomRecomNewYork.txt",
    "clases\\Recomendaciones\\PopularityRecommendationsNewYork.txt",
    "clases\\Recomendaciones\\KNNRecommendations_K20NewYork.txt"]


validation_data_path = "subsets\\NewYork_US_validation.txt"
train_data_path = "subsets/NewYork_US_train.txt"
cutoff = 10

algorithm_names = ["Random", "Popularity", "K20"]

data = {"Algorithm": [], "Precision": [], "Recall": [], "epc": [], "AggDiversity": []}

for i, rec_path in enumerate(rec_paths):
    prec, rec, epc, agg = evaluate_algorithm(rec_path, validation_data_path, train_data_path, 10)
    data["Algorithm"].append(algorithm_names[i])
    data["Precision"].append(prec)
    data["Recall"].append(rec)
    data["epc"].append(epc)
    data["AggDiversity"].append(agg)

table = pd.DataFrame(data)

print(table)





