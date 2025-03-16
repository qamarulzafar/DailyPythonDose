# ADDITION

a = "Qamar"
b = "Zafar"

print(a , b)

# Subtraction

a = 20
b = 10

print(a - b)

# Multiplication

a = 2
b = 10

print(a * b)

# Division

a = 4
b = 10

print(a / b)

# Modulus


a = 2
b = 10

print(a % b)

# Exponentiation

a = 2
b = 2

print(a ** b)

# Floor Division

a = 12
b  = 3

print(a // b)



#Solve Some questions about airthmetic_operators


# Q1

num = 17  
# Yeh check karein ke num even hai ya odd, aur uska result print karein.


if num % 2 == 0 :
    print("The Number is Even")
else:
    print("The number is Odd")




# Q2

num = -10  
# Yeh check karein ke num positive hai, negative hai, ya zero hai, aur result print karein.


if num < 0:
    print("Number is negetive")
elif num > 0 :
    print("Number is Positive")
else:
    print("Number is 0 ")




#  Q3

num = 24  
# Yeh check karein ke num 3 aur 5 dono se divisible hai ya nahi.


if num % 3 == 0 and num % 5 == 0:
    print("Number 3 and 5 is divisible ")
else :
    print("Number 3 and 5 is not divisible")



# Q4

a = 5  
b = 8  
# a aur b ko swap karein bina kisi extra variable ke.


a, b = b, a

print("a :", a)
print("b :", b)