# Python Functions


# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


# Creating a Function
# In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")


# Calling a Function
# To call a function, use the function name followed by parenthesis:


def my_function():
  print("Hello from a function")

my_function()




# Arguments


# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:



def my_function(fname):
    print(fname + "Zafar")

my_function("Khizra")
my_function("Qamar")
my_function("Rafay")



# Parameters or Arguments?

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.




# Number of Arguments

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.




def my_function(fname, lname):
   print(fname, " ", lname)

my_function("Qamar", "Zafar")



# If you try to call the function with 1 or 3 arguments, you will get an error:


def my_function(fname, lname):
  print(fname + " " + lname)

# my_function("Emil")




# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:




def my_function (*kids):
   print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")



# Keyword Arguments

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.


def my_function(child3, child2, child1):
   print("The youngest child is " + child3)

my_function(child1="Qamar", child2="Khizra", child3="Rafay")





# Arbitrary Keyword Arguments, **kwargs


# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:




def myfunction(**kids):
   print("His last name is ", kids["lname"])

myfunction(fname = "Qamar", lname = "Zafar")




# Default Parameter Value

# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:


def my_function(countery = "Norway"):
   print("I am from " + countery)

my_function("Sweden")
my_function("Pakistan")
my_function()



# Passing a List as an Argument

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:




def my_function(food):
   for x in food:
    print(x)

fruits = ["Banana", "Mango", "Apple"]
my_function(fruits)



# Return Values
# To let a function return a value, use the return statement:


def my_function(x):
   return 5 * x

print(my_function(3))
print(my_function(2))
print(my_function(1))





# The pass Statement

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.



def my_function():
   pass




# Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
   print(x + 1)

my_function(3)



# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:



def my_function(x):
  print(x)

my_function(x = 3)


# But when adding the , / you will get an error if you try to send a keyword argument:


def my_function(x, /):
  print(x)

# my_function(x = 3)



# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:




def my_function(*, x):
   print(x + 2)


my_function(x = 3)


# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:



def my_function(x):
  print(x)

my_function(3)



# But with the *, you will get an error if you try to send a positional argument:



def my_function(*, x):
  print(x)

# my_function(3)




# Combine Positional-Only and Keyword-Only

# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.



def my_function(x, y, /, * , a, b):
   print(x + y + a + b)


my_function(5, 6, a = 2, b = 3)






def calculate_grade(name, marks, total_marks=100):
    percentage = (marks / total_marks) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return f"Student: {name}\nMarks: {marks}/{total_marks}\nPercentage: {percentage:.2f}%\nGrade: {grade}"

# Call the function
print(calculate_grade("Ali", 87))
print()
print(calculate_grade("Sara", 45, 80))
