# Python Lists


mylist = ["apple", "banana", "cherry"]


# List

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)


# List Items

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.




# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# List Length
# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))



# List Items - Data Types
# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
list3 = [True, False, True, False, True]

print(list1)
print(list2)
print(list3)


# A list can contain different data types:

list4 = ["apple", 12, True, None]
print(list4)


# type()
# From Python's perspective, lists are defined as objects with the data type 'list':

# <class 'list'>


mylist = ["apple", "banana", "cherry"]
print(type(mylist))



# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry"))
print(thislist)



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.