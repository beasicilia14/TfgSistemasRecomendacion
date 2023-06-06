import datetime

cities = ("NewYork_US", "Tokyo_JP")
for city in cities: 

    file_write_name = "dataProcessingGowalla\\intermediateFiles\\" + city + "_train.txt"
    file_name = "dataProcessingGowalla\\intermediateFiles\\" + city + "checkins.txt"
    
    file_write = open(file_write_name, "w")

    with open(file_name) as file: 
        for line in file: 
            line_split = line.split("\t")
            date = line_split[1]
            dt = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

            # Convert the datetime object to a Unix timestamp
            timestamp = int(dt.timestamp())

            #fpursquare: user_id   id_poi type timestamp lat lon 
            #gowalla: user_id timestamp lat lon id_poi 

            id_poi = line_split[4].split("\n")[0]
            lat = line_split[2]
            lon = line_split[3]


            file_write.write(line_split[0] + "\t" + id_poi + "\t" + "Undefined category" + "\t" + str(timestamp) + "\t" + lat + "\t" + lon + "\n" )

