"""
Author: Elijah Asante
Purpose: Data Analysis
"""

# These variables are to store filtered info per entry from user
countries = []
life_expectancies = []
years = []

# These variables are to store the entire dataset compartments even after splitting them
all_countries = []
all_years = []
all_life_expectancies = []

while True:
# Ask the user for the year
    user_input = int(input("Enter the year of interest: "))
    
# Open the file
    with open("life-expectancy.csv") as analyzer:

# Skip the header
        next(analyzer)

# Read each line
        for line in analyzer:

# Split names
            split_line = line.strip().split(",")

# Store them in variables
            country = split_line[0]
            initials = split_line[1]
            year = int(split_line[2])
            life_expectancy = float(split_line[3])

# Store all dataset particulars in these variables for the overall analysis
            all_countries.append(country)
            all_years.append(year)
            all_life_expectancies.append(life_expectancy)

# Check whether this is the year selected by the user
            if year == user_input:

# Pack the need details into list containers countries and life_expectancies
                countries.append(country)
                life_expectancies.append(life_expectancy)
                years.append(year)
# Overall maximum
        overall_max = max(all_life_expectancies)
        max_index = all_life_expectancies.index(overall_max)

        max_country = all_countries[max_index]
        max_year = all_years[max_index]


# Overall minimum
        overall_min = min(all_life_expectancies)
        min_index = all_life_expectancies.index(overall_min)

        min_country = all_countries[min_index]
        min_year = all_years[min_index]


# Checking if data for the selected year was found 
    if len(life_expectancies) > 0:


# Calculate the average
        average = sum(life_expectancies) / len(life_expectancies)

# Apply the min() and max() functions on the variable - life_expectancies
        highest = max(life_expectancies)
        lowest = min(life_expectancies)

# Find the countries with those values using the index() method
        highest_index = life_expectancies.index(highest)
        lowest_index = life_expectancies.index(lowest)

        highest_country = countries[highest_index]
        lowest_country = countries[lowest_index]

# Print the results
        print(f"The overall max life expectancy is: {overall_max} from {max_country} in {max_year}")
        print(f"The overall min life expectancy is: {overall_min} from {min_country} in {min_year}")
        print()
        print(f"For the year {user_input}")
        print(f"Average life expectancy: {average:.2f} years")
        print(f"Highest life expectancy: {highest_country} - {highest:.2f} years")
        print(f"Lowest life expectancy: {lowest_country} - {lowest:.2f} years")
    else: 
        print(f"No data found for {user_input}.")