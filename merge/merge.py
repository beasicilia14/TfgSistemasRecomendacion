
#updating 

cities = ("NewYork_US", "Tokyo_JP")


for city in cities: 
  # Define the filenames
    file_foursquare = "subsets\\" + city +"_train_completo.txt"
    file_gowalla = "dataProcessingGowalla\\" + city + "Filtered&Grouped.txt"

    output_file = "merge\\" + city + "FoursquareGowalla_train.txt"

# Open the files
    with open(file_foursquare, "r") as f1, open(file_gowalla, "r") as f2, open(output_file, "w") as output:
    # Write the contents of file1 to the output file
        output.write(f1.read())   
    # Write the contents of file2 to the output file
        output.write(f2.read())


for city in cities: 
  # Define the filenames0
    file_foursquaregowalla = "merge\\" + city +"FoursquareGowalla_train.txt"
    file_brightkite = "dataProcessingBrightKite\\" + city + "Filtered&Grouped.txt"

    output_file = "merge\\" + city + "FoursquareGowallaBrightkite_train.txt"

# Open the files
    with open(file_foursquaregowalla, "r") as f1, open(file_brightkite, "r") as f2, open(output_file, "w") as output:
    # Write the contents of file1 to the output file
        output.write(f1.read())   
    # Write the contents of file2 to the output file
        output.write(f2.read())