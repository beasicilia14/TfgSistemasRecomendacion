

cities = ("NewYork_US", "Tokyo_JP")


for city in cities: 
  # Define the filenames
    file_foursquare = "subsets\\" + city +"_train.txt"
    file_gowalla = "dataProcessingGowalla\\" + city + "_train.txt"

    output_file = "merge\\" + city + "merged_train.txt"

# Open the files
    with open(file_foursquare, "r") as f1, open(file_gowalla, "r") as f2, open(output_file, "w") as out:
    # Write the contents of file1 to the output file
        out.write(f1.read())   
    # Write the contents of file2 to the output file
        out.write(f2.read())