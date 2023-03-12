
#PRECISION y RECALL SENCILLO. COMPARAMOS TEST  Y VALIDATION Y DIVIDIMOS ENTRE K 
#luego habrá que juntar todo 

import statistics 

def getPrecisionRecall(testSet, recommendations):
    
    with open(testSet) as file: 
        diccionario ={}
        for line in file: 
            line_split = line.split("\t")
            user=line_split[0]
            poi=line_split[1]

            if user in diccionario.keys(): 
                diccionario[user].append(poi)
            else: 
                diccionario[user] = [poi]
            
    #Tenemos diccionario con user: [poi1, poi2...]

    with open(recommendations) as popularityFile: 
        diccionario_pop ={}
        for line in popularityFile: 
            line_split = line.split("\t")
            user= line_split[0]
            poi=line_split[2]
            poi=poi.split("\n")[0]
            if user in diccionario_pop.keys(): 
                diccionario_pop[user].append(poi)
            else: 
                diccionario_pop[user] = [poi]

    count = 0 
    precision_dicc = {}
    recall_dicc = {}
    for i in diccionario.keys():
        if i in diccionario_pop.keys(): 
            pois_test = diccionario[i]
            pois_recommended = diccionario_pop[i]

            for j in pois_test: 
                if j in pois_recommended: 
                    count +=1 

            precision = count/len(pois_recommended) 
            recall = count/ len(pois_test)
            precision_dicc[i] = round(precision,2)
            recall_dicc[i] = round(recall,2)

        else: 
            pass


    prec_value = statistics.mean(precision_dicc.values())
    rec_value = statistics.mean(recall_dicc.values())


    return prec_value, rec_value