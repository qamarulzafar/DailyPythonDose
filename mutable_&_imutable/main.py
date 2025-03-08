# Mutable

my_list = [1, 2, 3]
print(id(my_list))  # Memory address before modification
my_list.append(4)
print(id(my_list))  # Memory address remains the same


#immutable

my_str = "Hello"
print(id(my_str))  # Memory address before modification
my_str += " World"  # Creates a new object
print(id(my_str))  # New memory address
