"""
Author: Elijah Asante
Purpose: Data Analysis
"""
percentages = []
entity_years = []
countries = []

while True:
# Open the file
    with open("life-expectancy.csv") as analyzer:

    # Skip the header of the dataset
        next(analyzer)

    # Read the file
        for line in analyzer:

    # Split the data into individual parts
            parts = line.strip().split(",")

    # Store each part into a variable
            entity = parts[0]
            code = parts[1]
            year = int(parts[2])
            expectancy = float(parts[3])

    # Pack them in list containers for easy use
            countries.append(entity)
            entity_years.append(year)
            percentages.append(expectancy)
            
            

    # Find and store the overall min and overall max results into individual variables
        overall_lowest = min(percentages)
        overall_highest = max(percentages)

    # Take user input
        user_input = int(input("Enter the year of interest: "))

    # Print the results
        print(f"The overall min life expectancy is: {overall_lowest}")
        print(f"The overall max life expectancy is: {overall_highest}")

        average = sum(percentages) / len(percentages)
        highest_index = percentages.index(overall_highest)
        lowest_index = percentages.index(overall_lowest)

        highest_country = countries[highest_index]
        lowest_country = countries[lowest_index]

         
        found = False  
        for year in entity_years:
            if year == user_input:
                found = True
                break
        if found:
            print(f"For the year {user_input}:")
            print(f"The average life expectancy across all countries was {average:.2f}")
            print(f"The max life expectancy was in {highest_country} with {highest_index:2f}")
            print(f"The min life expectancy was in {lowest_country} with {lowest_index:2f}")
        else:
            print(f"{user_input} not found in this dataset")

            
            
            