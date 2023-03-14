
#EPC Expected popularity complement 
#Formula calculada ara cada usuario 
#Cogemos las n primeras recomendaciones y por cada recomendacion 
#se calcula el número de visitas de ese POI en entrenamiento (total de usuarios de entrenamiento)

#calculo para cada recomendacion y se hace la media 

#epc por usuario es 1-valor 


#EPC mide la novedad d elos elementos recomendados
#Calcula dentro de los elementos recomendados si han sido valorados por el resto de usuarios 
#Si si han sido vaorados, son los más populares o exitosos 

#Cuanto más popular es un item, menos novedosa es la recomendacion 

#EPC(usuario)= 1/k * sum(1-pop(ik))

#numero visitas EN ENTRENAMIENTO 

from readTrain import readTrain
import statistics 

def epc(recommendations, trainset, cutoff): 
    pois, scores , city = readTrain(trainset)
    #pois tenemos usuario_Train: poi1, poi2.... 
    #scores tenemos poi1:score1, poi2:score2

    epc_dicc={}
    dicc_recommendations = {}

    with open(recommendations) as file1: 
        for line in file1: 
            line_split = line.split("\t")
            #0 user, 1 ranking , 2 poi
            user = int(line_split[0])
            poi = int(line_split[2])

            if user not in dicc_recommendations: 
                dicc_recommendations[user] = set([poi])
                    
            else: 
                if len(dicc_recommendations)<cutoff: 
                 dicc_recommendations[user].add(poi)

            #tenemos diccionario con los lugares visitados por CADA usuario 
        

        for user in dicc_recommendations: 
            lista = []
            visited_pois = dicc_recommendations[user]
            
            for i in visited_pois:
                lista.append(scores[i]/len(dicc_recommendations))

            epc = 1- sum(lista)/len(lista)

            epc_dicc[user] = epc 
    
    return statistics.mean(epc_dicc.values())

    
    
    
    
    