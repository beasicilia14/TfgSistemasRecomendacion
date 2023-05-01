cities = ("NewYork_US", "Tokyo_JP")

for city in cities: 
    dicc_bk= {}

    file_name = "dataProcessingBrightkite\\intermediateFiles\\equivalencias_" + city + ".txt"

    with open(file_name) as file: 
        for line in file: 
            line_split = line.split("\t")
            id_foursquare = line_split[1].split("\n")[0]
            id_bk = line_split[0]
        
            # 0:id gowalla 
            #1: id foursquare 
            dicc_bk[id_bk] = id_foursquare

    
    file_name_w = "dataProcessingBrightkite\\intermediateFiles\\" + city + "_train.txt" 
    writefile = open(file_name_w,  "w")
    count = 0 

    file_name_2 = "dataProcessingBrightkite\\intermediateFiles\\" + city + "_checkins.txt"

    with open(file_name_2) as file2: 
        for line in file2: 
            line_split = line.split("\t")
            #0: id user 
            #1: poi id
            #4: id poi 
            id_poi_bk = line_split[1]
          
            #estructura train: userid poiid timestamp lat lon num
            if id_poi_bk in dicc_bk.keys(): 
                count +=1
                writefile.write(line_split[0] + "\t" +  dicc_bk[id_poi_bk] + "\t" +  line_split[2] + "\t" + line_split[3] + "\t" + line_split[4])

