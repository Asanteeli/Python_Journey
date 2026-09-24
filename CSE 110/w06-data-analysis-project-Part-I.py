"""
Author: Elijah Asante
Purpose: Data Analysis
"""
percentages = []
# Open the file
with open("life-expectancy.csv") as analyzer:

    next(analyzer)  # This line eliminates the content of the hearder row

# Read the file
    for line in analyzer:

# Split names
        split_line = line.strip().split(",")

# Store them in variables
        country = split_line[0]
        initials = split_line[1]
        year_expectancy = split_line[2]
        percentage = split_line[3]

# Pack the various percentages into a list container called percentages
        percentages.append(percentage)

# Apply the min() and max() functions on the container
lowest = min(percentages)
highest = max(percentages)


# Print the results
print(f" The lowest value for life expectancy is {lowest}")
print(f" The highest value for life expectancy is {highest}")

