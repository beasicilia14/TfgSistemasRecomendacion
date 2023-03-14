#AGGREGATE DIVERSITY METRIC 
#Aggregate diversity is a metric that evaluates the diversity of a set of recommended
#items for a group of users. The metric measures how diverse the recommended items are
#across all users.

#For each user, we will take the first n recommendations and put them in a set (SET doesnt admit duplicates)



def aggregateDiversity(recommendations, cutoff): 
    dicc_recommendations ={}
    
    pois_set = set()
   
    with open(recommendations) as file: 
        for line in file: 
            line_split = line.split("\t")
            user = int(line_split[0])
            poi = int(line_split[2])
            
            if user not in dicc_recommendations.keys(): 
                dicc_recommendations[user] = set([poi])
            else: 
                if len(dicc_recommendations[user])<cutoff: 
                    dicc_recommendations[user].add(poi)

            for i in dicc_recommendations[user]: 
                pois_set.add(i)
            
    return len(pois_set) 