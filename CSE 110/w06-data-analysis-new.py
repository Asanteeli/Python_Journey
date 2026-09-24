years = []
countries = []
expectancy_years = []

# State a condition for a while loop
while True:
# Ask user for input
    user_input = input("Enter the year of interest: ")

# Open the CSV file
    with open("life-expectancy.csv") as analyzer:

# Skip heading
        next(analyzer)

# Read the file
        for line in analyzer:

# Break or split the components of the line into parts and store it into a variable
            parts = line.strip().split(",")

# Categorize the parts into lists
            country = parts[0]
            year = parts[2]
            expectancy = parts[3]

# Compare user input with years list
            if year == user_input:
# Update the various lists before the individual analysis
                 countries.append(country)
                 years.append(year)
                 expectancy_years.append(expectancy)
        if len(expectancy_years) > 0:

# Calculate the average
                # average = sum(expectancy_years) / len(expectancy_years)

# Find the overall max and min for the life expectancy years and store in variables
                overall_lowest = min(expectancy_years)
                overall_highest = max(expectancy_years)

# Print the output for max and min expectancy
                print(f"The overall max life expectancy is: {overall_highest} from ")
                print(f"The overall min life expectancy is: {overall_lowest} from ")
