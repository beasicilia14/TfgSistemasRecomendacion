# estructura checkins file [user]   [check-in time]	[latitude]	[longitude]	[location id]

#hay que: 
#mirar long lat, hacer fichero pois nyc y pois tokyo 
#cuando tenga eso cambiar user id , equivalencias, timestamp cambiar 

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

#GETTING INFO ABOUT CITIES USING FOURSQUARE DATASET.. 
dicc_ciudades ={}
ciudades = ("NewYork_US", "Tokyo_JP" )
with open("datasets\\foursquare\\dataset_TIST2015_Cities.txt") as file: 
    for line in file: 
        split_line = line.split("\t")
        # 0: nombre ciudad / 1: latitud / 2: Longitud /3: Codigo Pais /4: Nombre /5: tipo 
        city = split_line[0].replace(" ","") + "_" + split_line[3]

        if city in ciudades: 
            dicc_ciudades[city] = [float(split_line[1]), float(split_line[2])]

dicc_asignados ={}

for city in ciudades: 
    dicc_asignados[city] = set()
    with open("datasets\\brightkite\\Brightkite_totalCheckins.txt") as file_brightkite:
        for line in file_brightkite: 
            line_split = line.split("\t")
            #user]   [check-in time]	[latitude]	[longitude]	[location id]

            #poi id is 4 
            #lat is 2
            #lon is 3 

            poi_id = line_split[4].split("\n")[0]
            if line_split[2]=='': 
                lat = 0.0
            else: 
                lat = float(line_split[2])
            
            if line_split[3]=='': 
                lon = 0.0
            else: 
                lon = float(line_split[3])
            
        
            #print(lon)
            distance = haversine(lat, lon, dicc_ciudades[city][0], dicc_ciudades[city][1])

            if distance <30: 
                dicc_asignados[city].add(poi_id)


#dicc asignados 
import datetime

for city in ciudades: 
    pois_city = dicc_asignados[city]
    file_write = open("dataProcessingBrightkite\\intermediateFiles\\" + city.replace(" ", "") + "_checkins.txt", "w")
    
    with open("datasets\\brightkite\\Brightkite_totalCheckins.txt") as file_brightkite:
        
        for line in file_brightkite: 
            line_split = line.split("\t")
            poi_id = line_split[4].split("\n")[0]

            if poi_id in pois_city: 
                dt = datetime.datetime.strptime(line_split[1], "%Y-%m-%dT%H:%M:%SZ")
            # Convert the datetime object to a Unix timestamp
                timestamp = int(dt.timestamp())
                file_write.write(line_split[0] + "bk" + "\t" + poi_id + "\t" + str(timestamp) + "\t" + line_split[2] + "\t" + line_split[3] + "\n") 

#user id, poi id, timestamp, lat, lon , score 


