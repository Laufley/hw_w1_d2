stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("edinburgh Waverley")
print(stops)

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
print(stops)

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.append(4, "Polmont")
print(stops)
#Question: Why is it 4th position and not 3rd? Counting starts at 0

#4. Print out the index position of "Linlithgow"
print(stops.index("Linlithgow"))

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print(stops)

#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
print(stops)

#7. Print the number of stops there are in the list
number_of_stops = len(stops)
print(number_of_stops)

#8. Sort the list alphabetically
sorted_stops = sorted(stops)
print(sorted_stops)

#9. Reverse the positions of the stops in the list
sorted_stops_reversed = sorted(stops, reverse = True)
print(sorted_stops_reversed)

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)
