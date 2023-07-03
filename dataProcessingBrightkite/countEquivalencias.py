
pois=set()
with open("dataProcessingBrightkite\\intermediateFiles\\equivalencias_NewYork_US.txt") as file: 
    for line in file: 
        line_split= line.split("\t")
        poi_foursquare = line_split[1]
        pois.add(poi_foursquare)

print(len(pois))