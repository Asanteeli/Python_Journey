# Lists to store data for the chosen year
countries = []
life_expectancies = []
while True:
    user_year = int(input("Enter the year of interest: "))

    with open("life-expectancy.csv") as analyzer:
        next(analyzer)   # Skip header

        for line in analyzer:
            parts = line.strip().split(",")

            country = parts[0]
            year = int(parts[2])
            expectancy = float(parts[3])

            # Keep only records from the chosen year
            if year == user_year:
                countries.append(country)
                life_expectancies.append(expectancy)

    # Check if the year exists
    if len(life_expectancies) == 0:
        print("Year not found.")

    else:
        average = sum(life_expectancies) / len(life_expectancies)

        highest = max(life_expectancies)
        lowest = min(life_expectancies)

        highest_index = life_expectancies.index(highest)
        lowest_index = life_expectancies.index(lowest)

        highest_country = countries[highest_index]
        lowest_country = countries[lowest_index]

        print(f"For the year {user_year}:")
        print(f"The average life expectancy was {average:.2f}")
        print(f"The max life expectancy was in {highest_country} with {highest:.2f}")
        print(f"The min life expectancy was in {lowest_country} with {lowest:.2f}")