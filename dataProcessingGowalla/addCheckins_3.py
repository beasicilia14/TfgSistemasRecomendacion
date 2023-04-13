cities = ("NewYork_US", "Tokyo_JP")

for city in cities: 
    dicc_gowalla = {}

    file_name = "dataProcessingGowalla\\equivalencias_" + city + ".txt"

    with open(file_name) as file: 
        for line in file: 
            line_split = line.split("\t")
            id_foursquare = line_split[1].split("\n")[0]
            id_gowalla = line_split[0]
        
            # 0:id gowalla 
            #1: id foursquare 
            dicc_gowalla[id_gowalla] = id_foursquare

    
    file_name_w = "dataProcessingGowalla\\" + city + "checkins.txt" 
    writefile = open(file_name_w,  "w")
    count = 0 

    file_name_2 = "dataProcessingGowalla\\fichero" + city + ".txt"

    with open(file_name_2) as file2: 
        for line in file2: 
            line_split = line.split("\t")
            #0: id user 
            
            #4: id poi 
            id_poi_gowalla_n = line_split[4].split("\n")
            id_poi_gowalla = id_poi_gowalla_n[0]

            if id_poi_gowalla in dicc_gowalla.keys(): 
                count +=1
                writefile.write(line_split[0] + "g" + "\t" +  line_split[1] + "\t" +  line_split[2] + "\t" + line_split[3] + "\t" + dicc_gowalla[id_poi_gowalla] + "\n")

