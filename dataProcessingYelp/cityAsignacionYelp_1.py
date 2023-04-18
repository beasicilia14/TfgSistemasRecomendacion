#estructura 
#dataset 1: poi_id user_id timestamp 
#dataset 2: poi_id lat lon


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
ciudades = ("New York", "Tokyo" )
with open("datasets\\foursquare\\dataset_TIST2015_Cities.txt") as file: 
    for line in file: 
        split_line = line.split("\t")
        # 0: nombre ciudad / 1: latitud / 2: Longitud /3: Codigo Pais /4: Nombre /5: tipo 
        city = split_line[0]
        
        if city in ciudades: 
            dicc_ciudades[city] = [float(split_line[1]), float(split_line[2])]


#Getting dictionaty that relates each POI with lon and lat 
dicc_coords = {}
dicc_asignados={}

for city in ciudades: 
    dicc_asignados[city] = set()
    with open("datasets\\yelp\\Yelp_poi_coos4.txt") as filecoords: 
        for line in filecoords: 
            line_split = line.split("\t")
            #0 poi id
            #1 lat 
            #2 lon 
            poi_id = line_split[0]
            lat = float(line_split[1])
            lon = float(line_split[2].split("\n")[0])
            distance = haversine(lat, lon, dicc_ciudades[city][0], dicc_ciudades[city][1])

            if distance <30: 
                dicc_asignados[city].add(poi_id)
                

print(dicc_asignados)








