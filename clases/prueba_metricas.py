from metrica_clase import * 

object_metrica = Metrica("clases\\Recomendaciones\\RandomRecomNewYork.txt","subsets\\NewYork_US_validation.txt", "subsets/NewYork_US_train.txt", 10)

prec= object_metrica.precision() 
rec = object_metrica.recall()
epc = object_metrica.epc()
agg = object_metrica.aggregateDiversity()

print("prec ", prec)
print("rec  ", rec)
print("epc  ", epc)
print("agg  ", agg)


