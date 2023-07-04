
from abc import ABC, abstractmethod
from recomendador_clase import * 
import statistics 

class Metrica_User(ABC):
    def __init__(self, recommendations_path, test_data_path, train_data_path, cutoff):
        self.recommendations_path = recommendations_path
        self.test_data_path = test_data_path
        self.train_data_path = train_data_path
        self.cutoff = cutoff

    @abstractmethod
    def calculate(self):
        pass

class Precision(Metrica_User): 
    def __init__(self, recommendations_path, test_data_path, train_data_path, cutoff):
        super().__init__(recommendations_path, test_data_path, train_data_path, cutoff)
    
    def calculate(self): 
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


class Recall(Metrica_User): 
    def __init__(self, recommendations_path, test_data_path, train_data_path, cutoff):
        super().__init__(recommendations_path, test_data_path, train_data_path, cutoff)
    
    def calculate(self): 
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

class Epc(Metrica_User): 
    def __init__(self, recommendations_path, test_data_path, train_data_path, cutoff):
        super().__init__(recommendations_path, test_data_path, train_data_path, cutoff)
    
    def calculate(self):
        obj_rec = Recomendador()
        pois, scores, city = obj_rec.readTrain(self.train_data_path)
        
        epc_dicc = {}
        dicc_recommendations = {}
        
        with open(self.recommendations_path) as file1:
            for line in file1:
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[2])
                
                if user not in dicc_recommendations:
                    dicc_recommendations[user] = set([poi])
                else:
                    if len(dicc_recommendations[user]) < self.cutoff:
                        dicc_recommendations[user].add(poi)
    
    # Resto del código...


                #tenemos diccionario con los lugares visitados por CADA usuario 
            
           
            for user in dicc_recommendations: 
                lista = []
                visited_pois = dicc_recommendations[user]
                #print(visited_pois)
                for i in visited_pois:
                    
                    lista.append(scores[int(i)]/len(dicc_recommendations))

                epc = 1- sum(lista)/len(lista)

                epc_dicc[user] = epc 
        
        return statistics.mean(epc_dicc.values())
    

class PrecisionCategorias(Metrica_User): 
    def __init__(self, recommendations_path, test_data_path, train_data_path, cutoff):
        super().__init__(recommendations_path, test_data_path, train_data_path, cutoff)
        
    def calculate(self, dataset_pois):
        lista = []
	#SACAR CATEGORIAS DE CADA POI 
        diccionario_categorias = {}
        with open(dataset_pois) as file: 
            for line in file: 
                line_split = line.split("\t")
                poi_id = int(line_split[1])
                categoria = line_split[2].strip()
                diccionario_categorias[poi_id] = categoria

        dicc_recommendations = {}
        dicc_usertest = {}
	
       # print(diccionario_categorias)
	#SACAR RECOMENDACIONES HECHAS PARA CADA USUARIO DE TEST
        with open(self.recommendations_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[2])
                if user not in dicc_recommendations.keys(): 
                    dicc_recommendations[user] = set([poi])
                else: 
                    if len(dicc_recommendations[user]) < self.cutoff: 
                        dicc_recommendations[user].add(poi)

	
	#SACAR PUNTOS VISITADOS POR LOS USUARIOS EN TEST
        with open(self.test_data_path) as file: 
            for line in file: 
                line_split = line.split("\t")
                user = int(line_split[0])
                poi = int(line_split[1])

                if user not in dicc_usertest.keys(): 
                    dicc_usertest[user] = set([poi])
                else: 
                    dicc_usertest[user].add(poi)

        contador = 0
	#POR CADA USUARIO EN RECOMENDACIÓN 
        for user in dicc_recommendations.keys(): 
	#Saco puntos visitados 
            values = dicc_usertest[user]
	#Sacar categorías de los puntos visitados por el usuario. 
            categorias_usuariotest = {}
            for i in values: 
                categoria = diccionario_categorias[i]
                #print(categoria)
                if categoria in categorias_usuariotest.keys(): 
                    categorias_usuariotest[categoria] +=1
                else: 
                    categorias_usuariotest[categoria]=1 
            recomendaciones=[]
            if user in dicc_recommendations.keys():
                recomendaciones = dicc_recommendations[user]
                        
            else: 
                    pass 
            
            count = 0 
            
            for poi in recomendaciones: 
                if poi in diccionario_categorias.keys():
                    categoria = diccionario_categorias[poi]
                else: 
                    categoria = "UNKNOWN"

                if categoria in categorias_usuariotest:
                    if categorias_usuariotest[categoria] >0: 
                        categorias_usuariotest[categoria] = categorias_usuariotest[categoria] -1 
                        count +=1 
            contador += count/self.cutoff
           
         
        precision_categorias = 0.0
        precision_categorias += contador /len(dicc_recommendations) 

        
        return precision_categorias
