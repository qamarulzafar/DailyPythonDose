# Python - Access Set Items

# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.


thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


# Check if "banana" is NOT present in the set:
    

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)



# Change Items
# Once a set is created, you cannot change its items, but you can add new items.


