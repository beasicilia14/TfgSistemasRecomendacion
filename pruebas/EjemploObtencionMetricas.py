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

#Aqui debemos incluir los ficheros de recomendación de los que queramos obtener sus métricas. 
rec_paths = [
    "pruebas//RecomendacionesFoursquareTestTokyo//HybridRecommendationTokyo.txt",  "pruebas//RecomendacionesFoursquareTestTokyo//RandomRecomTokyo.txt",
    ]


test_data_path = "subsets//Tokyo_JP_test.txt"
train_data_path = "subsets//Tokyo_JP_train_completo.txt"
cutoff = 10

#Creación de nombres para la tabla 
algorithm_names = []
for rec_path in rec_paths: 
    ultima_barra = rec_path.rfind("/")
    punto = rec_path.rfind(".")
    nombre_archivo = rec_path[ultima_barra + 1:punto]
    algorithm_names.append(nombre_archivo)


#Ruta del rchivo que contiene información sobre categorías: 
categories_path = "dataProcessingFoursquare/intermediateFiles/Tokyo_JPFiltered.txt"

data = {"Algorithm": [], "Precision": [], "Recall": [], "epc": [], "AggDiversity": [], "Coverage": [], "Precision Categories":[] }

for i, rec_path in enumerate(rec_paths):
    prec, rec, epc, agg, cov = evaluate_algorithm(rec_path, test_data_path, train_data_path, cutoff)
    object_cat = PrecisionCategorias(rec_path, test_data_path, train_data_path, cutoff)
    prec_cat = object_cat.calculate(categories_path)

    data["Algorithm"].append(algorithm_names[i])
    data["Precision"].append(prec)
    data["Recall"].append(rec)
    data["epc"].append(epc)
    data["AggDiversity"].append(agg)
    data["Coverage"].append(cov)
    data["Precision Categories"].append(prec_cat)
    
    
table = pd.DataFrame(data)

print(table)






