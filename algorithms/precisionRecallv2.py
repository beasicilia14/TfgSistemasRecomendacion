import statistics 

def get_precision_recall(test_set_file, recommendations_file):
    
    # Create dictionary with test set data
    test_set_dict = {}
    with open(test_set_file) as file: 
        for line in file: 
            line_split = line.split("\t")
            user=line_split[0]
            poi=line_split[1]

            if user in test_set_dict: 
                test_set_dict[user].append(poi)
            else: 
                test_set_dict[user] = [poi]
            
    # Create dictionary with recommendation data
    rec_dict = {}
    with open(recommendations_file) as file: 
        for line in file: 
            line_split = line.split("\t")
            user= line_split[0]
            poi=line_split[2]
            poi=poi.split("\n")[0]

            if user in rec_dict: 
                rec_dict[user].append(poi)
            else: 
                rec_dict[user] = [poi]
                
    # Calculate precision and recall for each user
    precision_dict = {}
    recall_dict = {}
    for user in test_set_dict.keys():
        if user in rec_dict:
            test_set_pois = test_set_dict[user]
            recommended_pois = rec_dict[user]
            count = len(set(test_set_pois) & set(recommended_pois))
            
            if len(recommended_pois) > 0:
                precision = count / len(recommended_pois)
            else:
                precision = 0.0
            recall = count / len(test_set_pois)
            precision_dict[user] = round(precision, 2)
            recall_dict[user] = round(recall, 2)
    
    # Calculate mean precision and recall
    mean_precision = statistics.mean(precision_dict.values())
    mean_recall = statistics.mean(recall_dict.values())
    
    return mean_precision, mean_recall
