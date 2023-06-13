
pois = set()
with open("datasets\\brightkite\\Brightkite_totalCheckins.txt") as file: 
    for line in file: 
        line_split = line.split("\t")
        poi = line_split[4].strip()
        pois.add(poi)


print(len(pois))
