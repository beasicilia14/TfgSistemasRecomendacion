import json
import pandas as pd


dicc_pois = {}

with open('datasets\\yelpKaggle\\yelp_academic_dataset_business.json', "r", encoding="utf-8") as f:
    data = f.readlines()

for line in data:
    obj = json.loads(line)
    id = obj["business_id"]
    lat = obj['latitude']
    lon = obj['longitude']

    dicc_pois[id] = [lat, lon]
    


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

dicc_asignados={}

for city in ciudades: 
    dicc_asignados[city] = set()
    for i in dicc_pois.keys(): 
        lat = dicc_pois[i][0]
        lon = dicc_pois[i][1]

        distance = haversine(lat, lon, dicc_ciudades[city][0], dicc_ciudades[city][1])

        if distance <90: 
                dicc_asignados[city].add(i)
                


print(dicc_asignados)