from metrica_user_clase import * 
from metrica_test_clase import * 


import pandas as pd 

def evaluate_algorithm(rec_path, validation_data_path, train_data_path, k):
    object_prec = Precision(rec_path, validation_data_path,train_data_path,k)
    object_rec = Recall(rec_path, validation_data_path,train_data_path,k)
    object_epc = Epc(rec_path, validation_data_path,train_data_path,k)

    object_agg = AggregateDiversity(rec_path, validation_data_path, k)
    object_cov = Coverage(rec_path,validation_data_path, k )
    
    prec = object_prec.calculate()
    rec = object_rec.calculate()
    epc = object_epc.calculate()
    
    agg = object_agg.calculate()
    cov = object_cov.calculate()

    return prec, rec, epc, agg , cov

rec_paths = [
    "clases//Recomendaciones//RandomRecomNewYork.txt",
    "clases//Recomendaciones//PopularityRecommendationsNewYork.txt",
    "clases//Recomendaciones//KNNRecommendations_K20NewYork.txt", 
    "clases//Recomendaciones//KNNRecommendations_K30NewYork.txt", 
    "clases//Recomendaciones//KNNRecommendations_K60NewYork.txt", 
    "clases//Recomendaciones//KNN_MidpointRecommendations_K20NewYork.txt",
    "clases//Recomendaciones//KNN_MidpointRecommendations_K30NewYork.txt"]


validation_data_path = "subsets//NewYork_US_validation.txt"
train_data_path = "subsets/NewYork_US_train.txt"
cutoff = 10

algorithm_names = ["Random", "Popularity", "K20", "K30",  "K60", "K20 Midpoint", "K30 Midpoint"]

data = {"Algorithm": [], "Precision": [], "Recall": [], "epc": [], "AggDiversity": [], "Coverage": []}

for i, rec_path in enumerate(rec_paths):
    prec, rec, epc, agg, cov = evaluate_algorithm(rec_path, validation_data_path, train_data_path, 10)
    data["Algorithm"].append(algorithm_names[i])
    data["Precision"].append(prec)
    data["Recall"].append(rec)
    data["epc"].append(epc)
    data["AggDiversity"].append(agg)
    data["Coverage"].append(cov)

table = pd.DataFrame(data)

print(table)





