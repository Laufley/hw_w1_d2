united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom[1])

print(united_kingdom)

# I treated the dictionaries as arrays, and arrays start at int 0 
# Since there are no Key titles for every dictionary to refer to,
# I used the array int 1 as a key title to work on the second dictionary.


# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append(
{
  "name" : "Northern Ireland",
  "population" : 1811000,
  "capital" : "Belfast",
})

print(united_kingdom)


# 3. Use a loop to print the names of all the countries in the UK.
    for country in united_kingdom:
	print(country["name"])


#Also solved it it without a loop just to test things out
capital1 = (united_kingdom[0] ["capital"])
capital2 = (united_kingdom[1] ["capital"])
capital3 = (united_kingdom[2] ["capital"])

# 4. Use a loop to find the total population of the UK.
total = 0
for country in united_kingdom:
	total += country["population"]
print(total)