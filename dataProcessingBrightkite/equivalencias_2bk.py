import math
def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

cities = ("Tokyo_JP", "NewYork_US")

for city in cities: 
    file_namef  = "dataProcessingFoursquare\\intermediateFiles\\" + city + "finalVersion.txt" 
    
    dicc_brightkite = {}
    dicc_foursquare = {}

    city_bk = city.split("_")[0]
    file_name_brightkite = "dataProcessingBrightkite\\intermediateFiles\\" + city_bk + "_checkins.txt"


    with open(file_name_brightkite) as fileBrightkite: 
        for line in fileBrightkite: 
            #0 user 
            #1 id
            #2 timesp 
            #3 lat
            #4 lon 
           
            split_line = line.split("\t")

            id = split_line[1]
            lat = split_line [3]
            lon = split_line[4]

            if lat == "": 
                lat =0
            
            if lon == "":
                lon =0
            
            if id not in dicc_brightkite: 
                dicc_brightkite[id]  = [lat, lon]

    with open(file_namef) as fileFoursquare: 
        for line in fileFoursquare: 
            #2 lat
            #3 lon 
            #4 id 
            split_line = line.split("\t")

            id = split_line[1]
            lat = split_line [4]
            lon = split_line[5].split("\n")[0]
            
            if id not in dicc_foursquare: 
                dicc_foursquare[id]  = [lat, lon]


    file_name_final = "dataProcessingBrightkite\\intermediateFiles\\equivalencias_" + city_bk + ".txt"
    file = open(file_name_final, "a")

    equivalencias = {}
    #0.01 km 
    for i in dicc_brightkite: 
        lat_i = dicc_brightkite[i][0]
        lon_i = dicc_brightkite[i][1]

        valor= 5
        
        for j in dicc_foursquare: 
            lat_j = dicc_foursquare[j][0]
            lon_j = dicc_foursquare[j][1]
            if lat_j =="": 
                lat_j =0
            
            if lon_j =="": 
                lon_j = 0
            
            
            distancia = haversine(float(lat_i), float(lon_i),float(lat_j), float(lon_j)) 
            
            if distancia<valor: 
                valor = distancia 
                id_foursquare = j
    
        if valor <0.01: 
            file.write(str(i) + "\t" + str(id_foursquare) + "\n")
                    
    file.close()