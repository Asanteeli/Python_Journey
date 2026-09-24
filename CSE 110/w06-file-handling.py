# Open the file
with open("products.csv") as analyzer:

# Read through the file, line by line
 for line in analyzer:
    
# Split the line into parts
    parts = line.split(",")

# Store each part into a separate variable
    index = parts[0]
    name = parts[1]
    description = parts[2]
    brand = parts[3]
    catergory = parts[4]
    price = parts[5]
    currency = parts[6]
    stock = parts[7]
    ean = parts[8]
    color = parts[9]
    size = parts[10]
    availability = parts[11]
    internal_id = parts[12]

# Print the result
    print(f"The {index} and {name} have been printed")