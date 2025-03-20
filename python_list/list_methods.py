# Python - List Methods


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# 1) append() 

thislist = ["mango", "banana", "orange"]
thislist.append("cherry")
print(thislist)



# 2) clear() 

thislist = ["mango", "banana", "orange"]
thislist.clear()

print(thislist)


# 3) copy() 

thislist = ["mango", "banana", "orange"]
mylist = thislist.copy()

print(mylist)


# 4) count()

fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]
apple_count = fruits.count("apple")
print(apple_count)


# 5) extend() 

thislist = ["mango", "banana", "orange"]
fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

thislist.extend(fruits)
print(thislist)


# 6) index()

thislist = ["mango", "banana", "orange"]
print(thislist.index("orange"))


# 7) insert()

thislist = ["mango", "banana", "orange"]
thislist.insert(1, "kiwi")


print(thislist)



# 8 ) pop()

thislist = ["mango", "banana", "orange"]
thislist.pop(2)

print(thislist)


# 9) remove()

thislist = ["mango", "banana", "orange"]
thislist.remove("mango")

print(thislist)


# 10) reverse

thislist = ["mango", "banana", "orange"]
thislist.reverse()

print(thislist)



# 11) sort 


thislist = ["mango", "banana", "orange"]
thislist.sort()

print(thislist)