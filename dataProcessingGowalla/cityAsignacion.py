import math
def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia


#haversine devuelve distancia en kilómetros 
ciudades = ("New York", "Tokyo")
dicc_ciudades = {}
dicc_asignacion = {}

with open("datasets\\foursquare\\dataset_TIST2015_Cities.txt") as file: 
    for line in file: 
        split_line = line.split("\t")
        # 0: nombre ciudad / 1: latitud / 2: Longitud /3: Codigo Pais /4: Nombre /5: tipo 
        city = split_line[0]
        if city in ciudades: 
            dicc_ciudades[city] = [split_line[1], split_line[2]]


filePOIs_Nyc = open("dataProcessingGowalla\\ficheroNewYork.txt", "a")
filePOIs_Tky = open("dataProcessingGowalla\\ficheroTokyo.txt", "a")

with open("datasets\\gowalla\\Gowalla_totalCheckins.txt") as file2: 
    for line in file2: 
        #user, checkin_time, latitud, longitud, locationid 
        split_line = line.split("\t")
        latitud_poi = split_line[2]
        longitud_poi= split_line[3]

        for city in dicc_ciudades:
            dist = haversine(float(latitud_poi), float(longitud_poi), float(dicc_ciudades[city][0]), float(dicc_ciudades[city][1]))
            if dist <30: 
                ciudad_asignada = city 
                if ciudad_asignada == "New York": 
                    filePOIs_Nyc.write(str(split_line[0]) + '\t' + str(split_line[1]) + '\t' + str(split_line[2]) + '\t' + str(split_line[3]) + "\t" + str(split_line[4]) )
                else:
                    filePOIs_Tky.write(str(split_line[0]) + '\t' + str(split_line[1]) + '\t' + str(split_line[2]) + '\t' + str(split_line[3]) + "\t" + str(split_line[4]) )  
        
                # escribimos idnuevo + idantiguo + latitud + longitud + ciudad_CountryCode

filePOIs_Tky.close()
filePOIs_Nyc.close()





