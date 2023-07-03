import pandas as pd
from metrica_user_clase import PrecisionCategorias

test = "subsets/NewYork_US_test.txt"
train_data_path = "merge/NewYork_US_train_completo.txt"
cutoff = 10

rec_files = [
    "pruebas/RecomendacionesFoursquareTestNewYork/PopularityRecommendationsNewYork.txt",
    "pruebas/RecomendacionesFoursquareTestNewYork/PopularityMidpointRerankedRecommendationsNewYork.txt",
    "pruebas/RecomendacionesFoursquareTestNewYork/RandomRecomNewYork.txt",
    "pruebas/RecomendacionesFoursquareTestNewYork/RandomMidpointRerankedRecommendationsNewYork.txt",
    "pruebas/RecomendacionesFoursquareTestNewYork/KNN_k120RecommendationsNewYork.txt", 
    "pruebas/RecomendacionesFoursquareTestNewYork/KNN_K120MidpointRerankedRecommendationsNewYork.txt", 
    "pruebas/RecomendacionesFoursquareTestNewYork/KNN_MidpointRecommendations_k120NewYork.txt"
    # Agrega más rutas de archivo aquí para probar diferentes valores de rec
]

results = []

for rec in rec_files:
    
    object_prec_cat = PrecisionCategorias(rec, test, train_data_path, cutoff)
    categories_path = "dataProcessingFoursquare/intermediateFiles/NewYork_USFiltered.txt"
    prec_cat = object_prec_cat.calculate(categories_path)
    results.append((rec[-40:], prec_cat))

# Crear la tabla con los resultados
df = pd.DataFrame(results, columns=["Recomendaciones", "Precision de Categorias"])

# Imprimir la tabla
print(df)
