
cities = {}

    
while True:
    city = input("Enter the name of a city (or type 'stop' to finish): ").strip()
    if city.lower() == "stop":
        break
    if city:  #  si city est non vide
        cities[city] = len(city)  


sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)

    
print("Cities and their populations (sorted by population):")
for city, population in sorted_cities:
    print(f"{city}: {population} inhabitants")



