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
    "pruebas//RecomendacionesFoursquareValidation//RandomRecomNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//RandomMidpointRerankedRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//PopularityRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//PopularityMidpointRerankedRecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k20RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k30RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k40RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k50RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k60RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k100RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_k120RecommendationsNewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k20NewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k30NewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k40NewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k50NewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k60NewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k100NewYork.txt",
    "pruebas//RecomendacionesFoursquareValidation//KNN_MidpointRecommendations_k120NewYork.txt"

    ]


validation_data_path = "subsets//NewYork_US_validation.txt"
train_data_path = "subsets/NewYork_US_train.txt"
cutoff = 10

algorithm_names = ["Random", "Random Reranked","Popularity", "Popularity Reranked", "KNN K20", "KNN K30", "KNN K40", "KNN K50", "KNN K60", "KNN K100", "KNN K120", "Midpoint 20", "Midpoint 30", "Midpoint 40", "Midpoint 50", "Midpoint 60", "Midpoint 100", "Midpoint 120"]

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

output_file = "pruebas\\RecomendacionesFoursquareValidation\\NewYorkValidation_Metrics_Foursquare.csv"

# Write the DataFrame to Excel
table.to_csv(output_file, index=False)

print(table)





