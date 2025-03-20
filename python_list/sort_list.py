# Python - Sort Lists

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:


# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)



# Sort the list numerically:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)



# Sort Descending
# To sort descending, use the keyword argument reverse = True:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)



thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)



# Reverse Order


# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.



# Reverse the order of the list items:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


