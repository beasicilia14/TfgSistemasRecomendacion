#FILTRAMOS LAS CATEGORÍAS ELEGIDAS POR CIUDAD. 

import pandas as pd

#FILTERING CATEGORIAS
df_tokyo = pd.read_csv("dataProcessing//intermediateFiles//Tokyo_JP.txt", names = ["UserID", "VenueID", "Category", "TimeStamp", "Lat", "Lon"], sep="\t")
categories_tokyo = sorted(df_tokyo.Category.unique())
print(categories_tokyo)

df_nyc = pd.read_csv("dataProcessing//intermediateFiles//NewYork_US.txt", names = ["UserID", "VenueID", "Category", "TimeStamp", "Lat", "Lon"], sep="\t")
categories_nyc = sorted(df_nyc.Category.unique())
print(categories_nyc)

aceptadas_tokyo = ['Accessories Store', 'Afghan Restaurant', 'African Restaurant', 'American Restaurant', 'Animal Shelter', 'Antique Shop', 'Apres Ski Bar', 'Aquarium', 'Arcade', 'Arepa Restaurant', 'Art Gallery', 'Art Museum', 'Arts & Crafts Store', 'Arts & Entertainment', 'Asian Restaurant', 'Athletic & Sport', 'Athletics & Sports', 'Auditorium', 'Australian Restaurant', 'Automotive Shop', 'BBQ Joint', 'Bagel Shop', 'Bakery', 'Bank', 'Bar', 'Baseball Field', 'Baseball Stadium', 'Basketball Court', 'Basketball Stadium', 'Beach', 'Bed & Breakfast', 'Beer Garden', 'Bike Rental / Bike Share', 'Bike Shop', 'Board Shop', 'Boarding House', 'Boat or Ferry', 'Bookstore', 'Boutique', 'Bowling Alley', 'Brazilian Restaurant', 'Breakfast Spot', 'Brewery', 'Bridal Shop', 'Bridge', 'Building', 'Burger Joint', 'Burrito Place', 'Butcher', 'Caf\x1a', 'Caf\x1a\x1a', 'Cafeteria', 'Cajun / Creole Restaurant', 'Camera Store', 'Campground', 'Candy Store', 'Capitol Building', 'Car Dealership', 'Car Wash', 'Caribbean Restaurant', 'Casino', 'Castle', 'Cemetery', 'Cheese Shop', 'Chinese Restaurant', 'Church', 'City', 'City Hall', 'Climbing Gym', 'Clothing Store', 'Cocktail Bar', 'Coffee Shop', 'College & University', 'College Academic Building', 'College Administrative Building', 'College Arts Building', 'College Auditorium', 'College Bookstore', 'College Cafeteria', 'College Classroom', 'College Communications Building', 'College Engineering Building', 'College Football Field', 'College Gym', 'College History Building', 'College Lab', 'College Library', 'College Math Building', 'College Quad', 'College Rec Center', 'College Residence Hall', 'College Science Building', 'College Stadium', 'College Technology Building', 'College Theater', 'College Track', 'Comedy Club', 'Community College', 'Concert Hall', 'Conference Room', 'Convenience Store', 'Convention Center', 'Cosmetics Shop', 'Courthouse', 'Coworking Space', 'Credit Union', 'Cuban Restaurant', 'Cupcake Shop', 'Dance Studio', 'Deli / Bodega', 'Department Store', 'Design Studio', 'Dessert Shop', 'Dim Sum Restaurant', 'Diner', 'Distillery', 'Dive Bar', 'Dog Run', 'Donut Shop', 'Dumpling Restaurant',  'Eastern European Restaurant', 'Electronics Store','Embassy / Consulate',  'Ethiopian Restaurant', 'Event Space', 'Factory', 'Fair', 'Falafel Restaurant', 'Farm', 'Farmers Market', 'Fast Food Restaurant', 'Ferry', 'Field', 'Filipino Restaurant', 'Fire Station', 'Fish & Chips Shop', 'Fish Market', 'Flea Market', 'Flower Shop', 'Food', 'Food & Drink Shop', 'Food Court', 'Food Truck', 'Football Stadium', 'Fraternity House', 'French Restaurant', 'Fried Chicken Joint', 'Frozen Yogurt',  'Furniture / Home Store', 'Gaming Cafe', 'Garden', 'Garden Center','Gastropub', 'Gay Bar', 'General College & University', 'General Entertainment', 'General Travel', 'German Restaurant', 'Gift Shop', 'Gluten-free Restaurant', 'Golf Course', 'Gourmet Shop', 'Government Building', 'Greek Restaurant', 'Grocery Store', 'Gym', 'Gym / Fitness Center', 'Gym Pool', 'Harbor / Marina', 'Hardware Store', 'Health Food Store', 'High School', 'Hiking Trail', 'Historic Site', 'History Museum', 'Hobby Shop', 'Hookah Bar', 'Hostel', 'Hot Dog Joint', 'Hot Spring', 'Hotel', 'Hotel Bar', 'Hotel Pool','Hunting Supply', 'Ice Cream Shop', 'Indian Restaurant', 'Indie Movie Theater', 'Indie Theater', 'Indonesian Restaurant', 'Internet Cafe', 'Italian Restaurant','Japanese Restaurant', 'Jazz Club', 'Jewelry Store', 'Juice Bar', 'Karaoke Bar', 'Kids Store', 'Korean Restaurant', 'Lake', 'Latin American Restaurant', 'Law School', 'Library', 'Light Rail', 'Lighthouse', 'Lingerie Store', 'Liquor Store', 'Lounge', 'Mac & Cheese Joint', 'Malaysian Restaurant', 'Mall', 'Market', 'Martial Arts Dojo',  'Medical School', 'Mediterranean Restaurant', 'Meeting Room', "Men's Store", 'Mexican Restaurant', 'Middle Eastern Restaurant', 'Middle School', 'Military Base','Miscellaneous Shop', 'Mobile Phone Shop', 'Molecular Gastronomy Restaurant', 'Mongolian Restaurant', 'Monument / Landmark', 'Moroccan Restaurant', 'Mosque', 'Motel', 'Motorcycle Shop', 'Mountain', 'Movie Theater', 'Moving Target', 'Multiplex', 'Museum', 'Music School', 'Music Store', 'Music Venue', 'Nail Salon', 'Neighborhood', 'New American Restaurant', 'Newsstand', 'Nightclub', 'Nightlife Spot', 'Non-Profit', 'Opera House', 'Optical Shop', 'Other Great Outdoors', 'Other Nightlife', 'Outdoors & Recreation', 'Paella Restaurant', 'Paintball Field', 'Paper / Office Supplies Store', 'Park', 'Parking', 'Performing Arts Venue', 'Peruvian Restaurant', 'Pet Service', 'Pet Store', 'Photography Lab', 'Piano Bar', 'Pier', 'Pizza Place', 'Plane', 'Planetarium', 'Platform', 'Playground', 'Plaza', 'Police Station', 'Pool', 'Pool Hall', 'Portuguese Restaurant', 'Post Office', 'Professional & Other Places', 'Pub', 'Public Art', 'Racetrack', 'Radio Station', 'Ramen /  Noodle House', 'Record Shop', 'Recycling Facility','Rental Car Location','Resort', 'Rest Area', 'Restaurant', 'River', 'Road', 'Rock Climbing Spot', 'Rock Club', 'Roof Deck', 'Sake Bar', 'Salad Place', 'Salon / Barbershop', 'Sandwich Place', 'Scandinavian Restaurant', 'Scenic Lookout', 'Science Museum', 'Sculpture Garden', 'Seafood Restaurant', 'Shoe Store', 'Shop & Service', 'Shrine', 'Skate Park', 'Skating Rink', 'Smoke Shop', 'Snack Place', 'Soccer Field', 'Soccer Stadium', 'Sorority House', 'Soup Place', 'Southern / Soul Food Restaurant', 'Spa / Massage', 'Spanish Restaurant', 'Speakeasy', 'Spiritual Center', 'Sporting Goods Shop', 'Sports Bar', 'Stables', 'Stadium', 'Steakhouse', 'Strip Club', 'Student Center', 'Sushi Restaurant', 'Swiss Restaurant', 'Synagogue', 'Taco Place', 'Tailor Shop', 'Tanning Salon', 'Tapas Restaurant', 'Tattoo Parlor', 'Taxi', 'Tea Room', 'Temple', 'Tennis', 'Tennis Court', 'Thai Restaurant', 'Theater', 'Theme Park', 'Theme Park Ride / Attraction', 'Thrift / Vintage Store', 'Tourist Information Center', 'Toy / Game Store', 'Track', 'Track Stadium', 'Trade School', 'Travel Agency', 'Travel Lounge', 'Turkish Restaurant', 'University', 'Vegetarian / Vegan Restaurant', 'Veterinarian', 'Video Game Store', 'Video Store', 'Vietnamese Restaurant', 'Vineyard', 'Volcanoes', 'Voting Booth', 'Water Park', 'Well', 'Whisky Bar', 'Wine Bar', 'Wine Shop', 'Winery', 'Wings Joint', "Women's Store", 'Yoga Studio', 'Yogurt', 'Zoo']
aceptadas_nyc = ['Accessories Store', 'Afghan Restaurant', 'African Restaurant', 'Airport', 'American Restaurant', 'Animal Shelter', 'Antique Shop', 'Apres Ski Bar', 'Arcade', 'Arepa Restaurant', 'Argentinian Restaurant', 'Art Gallery', 'Art Museum', 'Arts & Crafts Store', 'Arts & Entertainment', 'Asian Restaurant', 'Athletic & Sport', 'Athletics & Sports', 'Auditorium', 'Australian Restaurant', 'Automotive Shop', 'BBQ Joint', 'Bagel Shop', 'Bakery', 'Bank', 'Bar', 'Baseball Field', 'Baseball Stadium', 'Basketball Court', 'Basketball Stadium', 'Beach', 'Bed & Breakfast', 'Beer Garden', 'Bike Rental / Bike Share', 'Bike Shop', 'Board Shop', 'Boat or Ferry', 'Bookstore', 'Boutique', 'Bowling Alley', 'Brazilian Restaurant', 'Breakfast Spot', 'Brewery', 'Bridal Shop', 'Bridge', 'Building', 'Burger Joint', 'Burrito Place', 'Butcher', 'Caf\x1a', 'Caf\x1a\x1a', 'Cafeteria', 'Cajun / Creole Restaurant', 'Camera Store', 'Campground', 'Candy Store', 'Capitol Building', 'Car Dealership', 'Car Wash', 'Caribbean Restaurant', 'Casino', 'Castle', 'Cemetery', 'Cheese Shop', 'Chinese Restaurant', 'Church', 'City', 'City Hall', 'Climbing Gym', 'Clothing Store', 'Cocktail Bar', 'Coffee Shop', 'College & University', 'College Academic Building', 'College Administrative Building', 'College Arts Building', 'College Auditorium', 'College Basketball Court', 'College Bookstore', 'College Cafeteria', 'College Classroom', 'College Communications Building', 'College Engineering Building', 'College Football Field', 'College Gym', 'College Lab', 'College Library', 'College Math Building', 'College Quad', 'College Rec Center', 'College Residence Hall', 'College Science Building', 'College Soccer Field', 'College Stadium', 'College Technology Building', 'College Theater', 'College Track', 'Comedy Club', 'Community College', 'Concert Hall', 'Conference Room', 'Convenience Store', 'Convention Center', 'Cosmetics Shop', 'Courthouse', 'Coworking Space', 'Credit Union', 'Cricket Ground', 'Cuban Restaurant', 'Cupcake Shop', 'Dance Studio', 'Deli / Bodega', 'Department Store', 'Design Studio', 'Dessert Shop', 'Dim Sum Restaurant', 'Diner', 'Distillery', 'Dive Bar', 'Dog Run', 'Donut Shop','Dumpling Restaurant', 'Eastern European Restaurant', 'Electronics Store', 'Elementary School', 'Embassy / Consulate','Ethiopian Restaurant', 'Event Space', 'Factory', 'Fair', 'Falafel Restaurant', 'Farm', 'Farmers Market', 'Fast Food Restaurant', 'Ferry', 'Field', 'Filipino Restaurant', 'Fire Station', 'Fish & Chips Shop', 'Fish Market', 'Flea Market', 'Flower Shop', 'Food', 'Food & Drink Shop', 'Food Court', 'Food Truck', 'Football Stadium', 'Fraternity House', 'French Restaurant', 'Fried Chicken Joint', 'Frozen Yogurt', 'Furniture / Home Store', 'Gaming Cafe', 'Garden', 'Garden Center','Gastropub', 'Gay Bar', 'General College & University', 'General Entertainment', 'General Travel', 'German Restaurant','Gift Shop', 'Gluten-free Restaurant', 'Golf Course', 'Gourmet Shop', 'Government Building', 'Greek Restaurant', 'Grocery Store', 'Gym', 'Gym / Fitness Center', 'Gym Pool', 'Harbor / Marina', 'Hardware Store', 'Health Food Store', 'Hiking Trail', 'Historic Site', 'History Museum', 'Hobby Shop', 'Hockey Arena', 'Hockey Field', 'Hookah Bar','Hostel', 'Hot Dog Joint', 'Hot Spring', 'Hotel', 'Hotel Bar', 'Hotel Pool', 'Ice Cream Shop', 'Indian Restaurant', 'Indie Movie Theater', 'Indie Theater', 'Indonesian Restaurant', 'Internet Cafe', 'Island', 'Italian Restaurant', 'Japanese Restaurant', 'Jazz Club', 'Jewelry Store', 'Juice Bar', 'Karaoke Bar', 'Kids Store', 'Korean Restaurant', 'Lake', 'Latin American Restaurant', 'Law School', 'Library', 'Light Rail', 'Lighthouse', 'Liquor Store', 'Lounge', 'Mac & Cheese Joint','Malaysian Restaurant', 'Mall', 'Market', 'Martial Arts Dojo', 'Medical Center', 'Medical School', 'Mediterranean Restaurant', 'Meeting Room', "Men's Store", 'Mexican Restaurant', 'Middle Eastern Restaurant', 'Middle School', 'Military Base', 'Miscellaneous Shop', 'Mobile Phone Shop', 'Molecular Gastronomy Restaurant', 'Mongolian Restaurant', 'Monument / Landmark', 'Moroccan Restaurant', 'Mosque', 'Motel', 'Motorcycle Shop', 'Movie Theater', 'Moving Target', 'Multiplex', 'Museum', 'Music School', 'Music Store', 'Music Venue', 'Nail Salon', 'Neighborhood', 'New American Restaurant', 'Newsstand', 'Nightclub', 'Nightlife Spot', 'Non-Profit', 'Opera House', 'Optical Shop', 'Other Great Outdoors', 'Other Nightlife', 'Outdoors & Recreation', 'Paella Restaurant', 'Paintball Field', 'Paper / Office Supplies Store', 'Park', 'Parking', 'Performing Arts Venue', 'Peruvian Restaurant', 'Pet Service', 'Pet Store', 'Photography Lab', 'Piano Bar', 'Pier', 'Pizza Place', 'Plane', 'Planetarium', 'Platform', 'Playground', 'Plaza', 'Police Station', 'Pool', 'Pool Hall', 'Portuguese Restaurant', 'Post Office', 'Professional & Other Places', 'Pub', 'Public Art', 'Racetrack', 'Radio Station', 'Ramen /  Noodle House', 'Real Estate Office', 'Record Shop', 'Recycling Facility', 'Rental Car Location', 'Residence', 'Residential Building (Apartment / Condo)', 'Resort', 'Rest Area', 'Restaurant', 'River', 'Road', 'Rock Climbing Spot', 'Rock Club', 'Roof Deck', 'Sake Bar', 'Salad Place', 'Salon / Barbershop', 'Sandwich Place', 'Scandinavian Restaurant', 'Scenic Lookout', 'School', 'Science Museum', 'Sculpture Garden', 'Seafood Restaurant', 'Shoe Store', 'Shop & Service', 'Shrine', 'Skate Park', 'Skating Rink', 'Ski Area', 'Ski Chairlift', 'Ski Chalet', 'Ski Lodge', 'Ski Trail', 'Smoke Shop', 'Snack Place', 'Soccer Field', 'Soccer Stadium', 'Sorority House', 'Soup Place', 'South American Restaurant', 'Southern / Soul Food Restaurant', 'Spa / Massage', 'Spanish Restaurant', 'Speakeasy', 'Spiritual Center', 'Sporting Goods Shop', 'Sports Bar', 'Stables', 'Stadium', 'Steakhouse', 'Storage Facility', 'Strip Club', 'Student Center', 'Surf Spot', 'Sushi Restaurant', 'Swiss Restaurant', 'Synagogue', 'Taco Place', 'Tailor Shop', 'Tanning Salon', 'Tapas Restaurant', 'Tattoo Parlor', 'Tea Room', 'Temple', 'Tennis', 'Tennis Court', 'Thai Restaurant', 'Theater', 'Theme Park', 'Thrift / Vintage Store', 'Tourist Information Center', 'Toy / Game Store', 'Track', 'Track Stadium', 'Trade School', 'Travel Agency', 'Travel Lounge', 'Turkish Restaurant', 'University', 'Vegetarian / Vegan Restaurant', 'Veterinarian', 'Video Game Store', 'Video Store', 'Vietnamese Restaurant', 'Vineyard', 'Volcanoes', 'Volleyball Court', 'Voting Booth', 'Water Park', 'Well', 'Whisky Bar', 'Wine Bar', 'Wine Shop', 'Winery', 'Wings Joint', "Women's Store", 'Yoga Studio', 'Yogurt', 'Zoo']

#LINE OF TOKYO 295	96292	Cosmetics Shop	1333491438.0
Tokyo_JP_Filtered = open('dataProcessing//intermediateFiles//Tokyo_JPFiltered.txt', 'w')  # fichero a escribir
with open("dataProcessing//intermediateFiles//Tokyo_JP.txt") as ficheropois:
    for line_poi in ficheropois:
        
        split_line = line_poi.split("\t")
        category = split_line[2]
        
        if category in aceptadas_tokyo:
            Tokyo_JP_Filtered.write(split_line[0] + '\t'+ split_line[1] + '\t'+ split_line[2] + '\t' + split_line[3] + '\t' + split_line[4] + "\t" + split_line[5])

        else: 
            pass        
Tokyo_JP_Filtered.close()


Nyc_US_Filtered = open('dataProcessing//intermediateFiles//NewYork_USFiltered.txt', 'w')  # fichero a escribir
with open("dataProcessing//intermediateFiles//NewYork_US.txt") as ficheropois:
    for line_poi in ficheropois:
        
        split_line = line_poi.split("\t")
        category = split_line[2]
        
        if category in aceptadas_nyc:
            Nyc_US_Filtered.write(split_line[0] + '\t'+ split_line[1] + '\t'+ split_line[2] + '\t' + split_line[3]  + '\t' + split_line[4] + "\t" + split_line[5])

        else: 
            pass 
Nyc_US_Filtered.close()


