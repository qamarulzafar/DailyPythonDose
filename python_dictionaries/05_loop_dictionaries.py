# Python - Loop Dictionaries


# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.



thisdic = {
    "name":"qamar",
    "age":19
}

for x in thisdic:
    print(x)


for x in thisdic:
    print(thisdic[x])


# You can also use the values() method to return values of a dictionary:


for x in thisdic.values():
    print(x)


# You can use the keys() method to return the keys of a dictionary:

for x in thisdic.keys():
  print(x)



# Loop through both keys and values, by using the items() method:

for x, y in thisdic.items():
  print(x, y)


    