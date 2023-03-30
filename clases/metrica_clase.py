import statistics #for epc 
from recomendador_clase import * 

class Metrica: 
    def __init__(self, recommendations_path, test_data_path, train_data_path, cutoff):
        self.recommendations_path = recommendations_path
        self.test_data_path = test_data_path
        self.train_data_path = train_data_path
        self.cutoff = cutoff

    #precision
    def precision(self): 
        dicc_recommendations ={}
        dicc_usertest = {}
    
        with open(self.recommendations_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                #print(line_split)
                user = int(line_split[0])
                poi = int(line_split[2])
                #print(poi)
                if user not in dicc_recommendations.keys(): 
                    dicc_recommendations[user] = set([poi])
                else: 
                    if len(dicc_recommendations[user])<self.cutoff: 
                        dicc_recommendations[user].add(poi)

    
        with open(self.test_data_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[1])

                if user not in dicc_usertest.keys(): 
                    dicc_usertest[user] = set([poi])
                else: 
                    dicc_usertest[user].add(poi)

        #Tenemos diccionario con usuario:recomendados, usuario:visitados 

    
        count=0 
    
        for user in dicc_recommendations.keys(): 
            #print(dicc_usertest[user])
            count+= len(dicc_recommendations[user] & dicc_usertest[user])/self.cutoff
        
        precision = count/len(dicc_recommendations)

        return precision 

    #recall
    def recall(self): 
        dicc_recommendations ={}
        dicc_usertest = {}
    
        with open(self.recommendations_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[2])
                
                if user not in dicc_recommendations.keys(): 
                    dicc_recommendations[user] = set([poi])
                else: 
                    if len(dicc_recommendations[user])<self.cutoff: 
                        dicc_recommendations[user].add(poi)

    
        with open(self.test_data_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[1])

                if user not in dicc_usertest.keys(): 
                    dicc_usertest[user] = set([poi])
                else: 
                    dicc_usertest[user].add(poi)

        #Tenemos diccionario con usuario:recomendados, usuario:visitados 
        count=0 
    
        for user in dicc_recommendations.keys(): 
            
            count+= len(dicc_recommendations[user] & dicc_usertest[user])/len(dicc_usertest[user])
        
        recall = count/len(dicc_recommendations)

        return recall 
    
    #epc
    def epc(self): 
        obj_rec = Recomendador()
        pois, scores, city = obj_rec.readTrain(self.train_data_path)
        
        epc_dicc={}
        dicc_recommendations = {}

        with open(self.recommendations_path) as file1: 
            for line in file1: 
                line_split = line.split("\t")
                #0 user, 1 ranking , 2 poi
                user = int(line_split[0])
                poi = int(line_split[2])

                if user not in dicc_recommendations: 
                    dicc_recommendations[user] = set([poi])
                        
                else: 
                    if len(dicc_recommendations)<self.cutoff: 
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
    
    #agg div 
    def aggregateDiversity(self): 
        dicc_recommendations ={}
        pois_set = set()
    
        with open(self.recommendations_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[2])
                
                if user not in dicc_recommendations.keys(): 
                    dicc_recommendations[user] = set([poi])
                else: 
                    if len(dicc_recommendations[user])<self.cutoff: 
                        dicc_recommendations[user].add(poi)

                for i in dicc_recommendations[user]: 
                    pois_set.add(i)
                
        return len(pois_set) 