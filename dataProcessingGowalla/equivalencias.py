
i = "NewYork_US"
file_name  = "dataProcessing\\intermediateFiles\\" + i + "finalVersion.txt" 

dicc_gowalla = {}
dicc_foursquare = {}

import math
def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia


with open("dataProcessingGowalla\\ficheroNewYork.txt") as fileGowalla: 
    for line in fileGowalla: 
        #2 lat
        #3 lon 
        #4 id 
        split_line = line.split("\t")

        id = split_line[4].split("\n")[0]
        lat = split_line [2]

        lon = split_line[3]
        
        if id not in dicc_gowalla: 
            dicc_gowalla[id]  = [lat, lon]

with open(file_name) as fileFoursquare: 
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



file = open("dataProcessingGowalla\\equivalencias.txt", "a")

equivalencias = {}
#0.01 km 
for i in dicc_gowalla: 
    lat_i = float(dicc_gowalla[i][0])
    lon_i = float(dicc_gowalla[i][1])

    valor= 5
    
    for j in dicc_foursquare: 
        lat_j = float(dicc_foursquare[j][0])
        lon_j = float(dicc_foursquare[j][1])
        
        distancia = haversine(lat_i, lon_i, lat_j, lon_j) 
        
        if distancia<valor: 
            valor = distancia 
            id_foursquare = j
   
    if valor <0.01: 
        file.write(str(i) + "\t" + str(id_foursquare) + "\n")
                
file.close()