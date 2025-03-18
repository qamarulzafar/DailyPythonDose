# Python Logical Operators
# Logical operators are used to combine conditional statements:


# ✅ 1. and Operator
# Agar dono conditions True hain to True return karega, warna False.


x = 5 
y = 10

result = (x > 2) and (y < 15)
print(result)

result = (x > 2) and (y > 15)
print(result)



# ✅ 2. or Operator
# Agar ek bhi condition True ho to True return karega. Sirf dono False hoon tabhi False hoga.


x = 5
y = 10

result  = (x > 2) or (y > 15)
print(result)

result = (x < 2) or (x > 15)
print(result)




# ✅ 3. not Operator
# Jo bhi condition ka result ho, usko ulta kar dega.

x = 5

result = not(x > 2)
print( result)

result = not(x < 2)
print(result)




# Logical Operators ka istemal if Statement mein


age = 20 
has_id = True

if age >= 18 and has_id:
    print("Aap enter kr skty h")
else:
    print("Access Denied")
    