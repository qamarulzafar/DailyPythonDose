# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:


# Add 10 to argument a, and return the result:


x = lambda a : a + 10
print(x(5))


# Lambda functions can take any number of arguments:

# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


def myfunc(n):
  return lambda a : a * n


# Example 3: Lambda Function as Argument

# Lambda functions can also be passed inside other functions.
# If a function multiplies a number by 3, and we use this function with map():

number = [1, 2, 3, 4, 5, 6]
doubled = list (map(lambda x: x* 3, number))

print(doubled)


# Example 4: Conditional Lambda Function
# An if-else statement can also be used inside a lambda function:



check_even = lambda x : "Even" if x % 2 == 0 else "odd"
print(check_even(12))










