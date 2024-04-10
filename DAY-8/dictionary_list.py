country = input("Enter Country Name\n")
visits = int(input("Number of Visits\n"))

# Create List From Formatted String
list_of_cities = eval(input("List of Cities\n"))
travel_log = [
    {
        "Country": "France",
        "Visits": 12,
        "Cities": ["paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "Visits": 5,
        "Cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've Been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My Favorite City Was {travel_log[2]['cities'][0]}.")
