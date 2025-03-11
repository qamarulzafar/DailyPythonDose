# Python - Modify Strings 

# Python has a set of built-in methods that you can use on strings.
# 
# Upper Case

a = "Hello, World"
print(a.upper())

# Lower Case

a = "HELLO, WORLD"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

a = " Hello World "
print(a.strip())

# Replace String
# The replace() method replaces a string with another string:

a = "Hello World"
print(a.replace("H", "T"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.


a = "Hello, World"
print(a.split(","))




