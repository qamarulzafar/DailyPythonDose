# Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:


# Example

print("Hello")
print("Hello")


# (Quotes Inside Quotes)
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("it's all right")
print("he is called 'johny'")
print('he is called "johny"')


# (Assign String to a Variable)

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello World"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)


# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)




# (Strings are Arrays)

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.


# Example
# Get the character at position 1 (remember that the first character has the position 0):


a = "Hello World"
print(a[1])


# (Looping Through a String)
# Since strings are arrays, we can loop through the characters in a string, with a for loop.


for x in "banana":
    print(x)



# (String Length)
# To get the length of a string, use the len() function.


a = "hello World"
print(len(a))



# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.


txt = "The  Best Thing in Life are free"
print("free" in txt)



# Use it in an if statement:


text = "The best Thing in Life are free"
if "free" in text:
    print("Yes, 'free' is Present")



# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.


text = "The best Thing in Life are free"
print("Expensive" not in text)


# Use it in an if statement:


text = "The best Thing in Life are free"
if "Expensive" not in text:
    print("No, 'Expence' is NOT present")

