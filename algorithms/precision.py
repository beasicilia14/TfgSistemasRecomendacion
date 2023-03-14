def precision(recommendations, testset, cutoff): 
    dicc_recommendations ={}
    dicc_usertest = {}
   
    with open(recommendations) as file: 
        for line in file: 
            line_split = line.split("\t")
            #print(line_split)
            user = int(line_split[0])
            poi = int(line_split[2])
            #print(poi)
            if user not in dicc_recommendations.keys(): 
                dicc_recommendations[user] = set([poi])
            else: 
                if len(dicc_recommendations[user])<cutoff: 
                    dicc_recommendations[user].add(poi)

  
    with open(testset) as file: 
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
        count+= len(dicc_recommendations[user] & dicc_usertest[user])/cutoff
    
    precision = count/len(dicc_recommendations)

    return precision 