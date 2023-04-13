from abc import ABC, abstractmethod

class Metrica_Test(ABC):
    def __init__(self, recommendations_path, test_data_path, cutoff):
        self.recommendations_path = recommendations_path
        self.test_data_path = test_data_path
        self.cutoff = cutoff

    @abstractmethod
    def calculate(self):
        pass

class AggregateDiversity(Metrica_Test): 

    def __init__(self, recommendations_path, test_data_path, cutoff):
        super().__init__(recommendations_path, test_data_path, cutoff)
    
    def calculate(self): 
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
    
class Coverage(Metrica_Test): 
    def __init__(self, recommendations_path, test_data_path, cutoff):
        super().__init__(recommendations_path, test_data_path, cutoff)

    def calculate(self): 
        #nºunique users in test 
        #nº unique users in recommendations 
        set_user_rec = set()
        set_user_test = set()

        with open(self.recommendations_path) as file_rec: 
            for line in file_rec: 
                line_split = line.split("\t")
                user_id = line_split[0]
                set_user_rec.add(user_id)
        
        with open(self.test_data_path) as file_test: 
            for line in file_test: 
                line_split = line.split("\t")
                user_id = line_split[0]
                set_user_test.add(user_id)
        
        return len(set_user_rec) / len(set_user_test)
        
