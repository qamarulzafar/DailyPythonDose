# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# There is also a method called get() that will give you the same result:


x = thisdict.get("model")



# Get Keys
# The keys() method will return a list of all the keys in the dictionary.


x = thisdict.keys()
print(x)


# Add a new item to the original dictionary, and see that the keys list gets updated as well:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)


car["color"] = "white"

print(x)


# Get Values
# The values() method will return a list of all the values in the dictionary.


x = thisdict.values()
print(x)


# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) 

car["year"] = 2020

print(x)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.


# Get a list of the key:value pairs


x = thisdict.items()
print(x)


# Make a change in the original dictionary, and see that the items list gets updated as well:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



# Add a new item to the original dictionary, and see that the items list gets updated as well:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



  