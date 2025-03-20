# Python - Join Lists


# Join Two Lists

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.


list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

list2 = list1 + list2
print(list2)



# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    

print(list1)



# Or you can use the extend() method, where the purpose is to add elements from one list to another list:


list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

