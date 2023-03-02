def readTrain(trainset):
    # Dictionary of POIs with visit counts

    pois ={}
    scores={}


    with open(trainset) as file2:
        for line in file2:
            split_line =line.split("\t")
            user_id=split_line[0]
            venue_id =split_line[1]

            if user_id not in pois.keys(): 
                pois[user_id] = [venue_id]
            else:
                pois[user_id].append(venue_id)

            if venue_id in scores.keys(): 
                scores[venue_id] += 1
            else:
                scores[venue_id] =1

    return pois, scores 
