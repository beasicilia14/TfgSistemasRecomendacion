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
    "pruebas//RecomendacionesFoursquareTestNewYork//RandomRecomNewYork.txt",
    "pruebas//RecomendacionesFoursquareTestNewYork//RandomMidpointRerankedRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareTestNewYork//PopularityRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareTestNewYork//PopularityMidpointRerankedRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareTestNewYork//KNN_k120RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareTestNewYork//KNN_k120MidpointRerankedRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareTestNewYork//KNN_MidpointRecommendations_k120NewYork.txt"

    ]


validation_data_path = "subsets//NewYork_US_test.txt"
train_data_path = "subsets/NewYork_US_train_completo.txt"
cutoff = 10

algorithm_names = ["Random", "Random Reranked","Popularity", "Popularity Reranked", "KNN K120", "KNN K120 Reranked", "KnnMidpoint 120"]

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





