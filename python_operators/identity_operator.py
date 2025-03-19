# Python Identity Operators 

# 🔹 Identity Operators Overview

# Python mein identity operators (is aur is not) ka use memory location compare karne ke liye hota hai. Yeh check karte hain ke do variables ek hi object ko refer kar rahe hain ya nahi.



# ✅ Identity Operators:

# is → True return karta hai agar dono variables same object ko refer kar rahe ho.
# is not → True return karta hai agar dono variables different objects ko refer kar rahe ho.




# 🔹 is Operator Example


x = [1,2,3]
y = x
z = [1,2,3]

print(x is y)
print(x is z)


# ✅ Explanation:

# x is y → True (same memory location)
# x is z → False (alag objects, bhale hi values same hain)



# 🔹 is not Operator Example


x = 10
y = 10 
z = 20

print(x is not y)
print(x is not z)


# ✅ Explanation:

# Python chhoti values (-5 se 256) ko cache karta hai, is wajah se x is y False hoga.
# x is not z → True hoga kyunki x aur z alag memory locations par hain.


# 🔹 Difference Between is and ==



# Operator                                   Function


# is                                         Memory location compare karta hai
# ==                                         Sirf values compare karta hai

# ✅ Explanation:

# == sirf values compare karta hai.
# is memory location compare karta hai.