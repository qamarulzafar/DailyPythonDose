## (Python Variables)

#Variables 
#Variables are containers for storing data values .


# (Creating Variables)

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.


x = 5 
y = 'qamar'

print(x)
print(y)


# Variables do not need to be declared with any particular type, and can even change type after they have been set.


a = 4             # x is of type int 
a = 'qamar'       # x is now of type str

print(a)



# (Casting)
# If you want to specify the data type of a variable, this can be done with casting.

b = str(1)    # b will be '3'
c = int(10)   # c will be 10 
d = float(3)  # d will be 3.0


# (Get the Type)
# You can get the data type of a variable with the type() function.


e = 100
f = 'python'

print(type(e))
print(type(f))



# (Single or Double Quotes?)
# String variables can be declared either by using single or double quotes:

g = "John"
 # is the same as 
h = 'john'


# (Case-Sensitive)
# Variable names are case-sensitive.


a = 1
A = "python"
# A will not overwrite a 

