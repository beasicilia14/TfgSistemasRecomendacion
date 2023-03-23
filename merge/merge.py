

cities = ("NewYork", "Tokyo")

for city in cities: 
    file_name = "merge\\" + city + "_train.txt"
    file_append = open(file_name, "a+") 

    file_gowalla = "dataProcessingGowalla\\" + city + "_train.txt"
    
    with open(file_gowalla) as file: 
        for line in file: 
            file_append.write(line)
