import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("all cities in Germany:")
for city in cities:
    if city['country'] == 'Germany':
        print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C:")
for city in cities:
    if float(city['temperature']) > 12 and city['country'] == 'Spain':
        print(city)
print()

# Count the number of unique countries
print("the number of unique countries:")
temps = []
for city in cities:
    if city['country'] not in temps:
        temps.append(city['country'])
print(len(temps))
print()

# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany:")
temps = [float(city['temperature']) for city in cities if city['country'] == 'Germany']
print(sum(temps) / len(temps))
print()

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy:")
temps = [float(city['temperature']) for city in cities if city['country'] == 'Italy']
print(max(temps))
print()

# Let's write a function to filter out only items that meet the condition
def filter(condition, dict_list):
    ret = []
    for item in dict_list:
        if condition(item):
            ret.append(item)
    return ret

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    tmp = []
    for item in dict_list:
        tmp.append(item[aggregation_key])
    return aggregation_function(tmp)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
aggregate_val = aggregate('temperature', lambda x: sum(map(float, x))/max(len(x),1), cities)
print(aggregate_val)
print()

# Print all cities in Germany
print("all cities in Germany:")
filtered_list = filter(lambda x: x['country'] == 'Germany', cities)
print(filtered_list)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C:")
filtered_list = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
print(filtered_list)
print()

# Count the number of unique countries
print("Count the number of unique countries: ")
aggregate_val = aggregate('country', lambda x: len({item for item in x}), cities)
print(aggregate_val)
print()

# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany: ")
filtered_list = filter(lambda x: x['country'] == 'Germany', cities)
aggregate_val = aggregate('temperature', lambda x: sum(map(float, x))/max(len(x), 1), filtered_list)
print(aggregate_val)
print()

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy: ")
filtered_list = filter(lambda x: x['country'] == 'Italy', cities)
aggregate_val = aggregate('temperature', lambda x: max(map(float, x)), filtered_list)
print(aggregate_val)
print()