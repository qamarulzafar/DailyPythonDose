# 🔹 Membership Operators in Python

# Membership operators ka use yeh check karne ke liye hota hai ke koi value list, tuple, string, dictionary, ya set mein mojood hai ya nahi.


# 🟢 Examples of in and not in


# 1) String k sath  

text  = "Hello, Python !"

print("P" in text)
print("Z" in text)
print("Python" in text)
print("Java" not in text)


# 2. List ke saath


fruits = ["apple", "mango", "banana"]
print("apple" in fruits)
print("graps" in fruits)
print("grape" not in fruits)



# 2. tuple ke saath


numbers = (1, 2, 3, 4, 5)

print(2 in numbers)
print(10 in numbers)
print(0 not in numbers)



# 4. Dictionary ke saath 

student = {
    "name" : "qamar",
    "age" : 19,
    "grade" : "A"
}

print("name" in student)
print("qamar" in student)  # ❌ False (values check nahi hoti)
print("age" not in student)


# Agar aapko values check karni hoon, to .values() use karein:

print("qamar" in student.values())



# 5. Set ke saath


colors = {"Red", "Blue", "green"}

print("Red" in colors)
print("yellow" not in colors)