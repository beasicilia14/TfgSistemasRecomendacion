import math 

def normalizeDicc(diccionario): 
    maximo = max(diccionario.values()) # valor máximo del diccionario
    minimo = min(diccionario.values()) # valor mínimo del diccionario
    
    if maximo != minimo:
    # por cada elemento normalizamos entre 0 y 1 ((valor-mínimo)/(máximo-mínimo))
        for poi in diccionario:
            diccionario[poi] = (diccionario[poi]-minimo) / (maximo-minimo)

    return diccionario

def haversine(lat1, lon1, lat2, lon2):
        rad=math.pi/180
        dlat=lat2-lat1
        dlon=lon2-lon1
        R=6372.795477598
        a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
        distancia=2*R*math.asin(math.sqrt(a))
        return distancia

