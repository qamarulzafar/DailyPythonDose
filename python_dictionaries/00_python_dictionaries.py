# Python Dictionaries

thisdic = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : 1964
}


# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])



# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)



# Dictionary Length
# To determine how many items a dictionary has, use the len() function:

print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}



# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))




# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.



thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


