# Going to print out cities and the country they are in

# First, a dictionary of cities and countries
ccs = {'Paris': 'France', 'New York': 'USA', 'Munich': 'Germany'}

# Then we write our function

def city_country(city, country):
    print(f"\nWe have {city} in the country of {country}!")

city_country(ccs.items[0], ccs.values[0])
