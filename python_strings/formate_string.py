# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age = 36
# txt = "My Name is John, And I am " + age
# print(txt)    # error

'''
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.'''


age = 19
txt = f"My name is Qamar , And I am {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.


price = 59
txt = f"The price is {price} dollars"
print(txt)


# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:


price = 1000.000
txt = f"The Price is {price:.2f} dollors"
print(txt)

tax = 1200.0000
ex = f"The tax is {tax:.3f}"
print(ex)

# A placeholder can contain Python code, like math operations:

# Example

text = f"The price is {20*30} dollors"
print(text)
