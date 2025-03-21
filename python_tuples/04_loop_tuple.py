# Python - Loop Tuples

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for x in fruits :
    print(x)


# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

for x in range(len(fruits)):
    print(fruits[x])




# Using a While Loop
# You can loop through the tuple items by using a while loop.

# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.



thistuple = ("apple", "banana", "mango")
i = 0

while i < len(thistuple):
    print(thistuple[i])
    i += 1


