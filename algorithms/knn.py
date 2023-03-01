
#algorithm calculates rating between users. 
#approach: 
    #1)Create a dictionary that has: user: {poi:score, poi2:score}
    #2) Get pois that user has visited 
    #3) if usertrain1 has visited any places == usertest its rating will improve. 

#dictionary to store: --> user:{poi1:score1, poi2:score2....}
#num: only comunes 
#den: todos y al cuadrado 


import math 

user_poi_scores = {}
user_test= "157785" #entra como parametro 
userSquaredSum = {} #poner sumatorio de score al cuadrado de cada uno 
similarity_scores  ={}

with open("subsets//NewYork_US_train.txt") as train:
        for line in train:
            split_line =line.split("\t")
            #0: user
            #1: poi
            #2: timestamp
            #3: score 
            user_id=split_line[0]
            poi =split_line[1]
            score = split_line[3]
            

            if user_id in user_poi_scores.keys(): 
                 user_poi_scores[user_id][poi] = int(score)
            else: 
                 user_poi_scores[user_id] = {int(poi):int(score)}

            #para denominador. 
            if int(user_id) not in userSquaredSum:
                userSquaredSum[int(user_id)] = int(score.strip())**2
            else:
                userSquaredSum[int(user_id)] += int(score.strip())**2


#Rating numerador --> sumatorio rui*rvi

#GET POIS VISITED BY USER_TEST:
if user_test in user_poi_scores.keys(): 
    user_visited = user_poi_scores[user_test]
else:
    user_visited =[]


#CALCULANDO SIMILITUD CON CADA UNO DE LOS USUARIOS. 

for user_train in user_poi_scores: 
    
    if user_train != user_test: 
    
        numerador =0 
        for poi in user_visited: 
            pois_train= user_poi_scores[user_train]

            if poi in pois_train: 
                numerador+= user_poi_scores[user_train][poi] * user_poi_scores[user_test][poi]
        
        #condition is necessary to ensure that both users have rated at least one POI
        #and their sum of squares is not zero, before computing the similarity between them.
        if int(user_train) in userSquaredSum and int(user_test) in userSquaredSum: 
            
            denominador = math.sqrt(userSquaredSum[int(user_train)] * userSquaredSum[int(user_test)])
            print(denominador)
            
        
            if numerador !=0: 
                similarity_scores[user_train]= numerador/denominador



      
      

