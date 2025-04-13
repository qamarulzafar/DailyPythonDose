import hashlib 


user = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    username = str(input("Enter Your Name: "))
    password = str(input("Enter Your Password: "))

    user[username] = hash_password(password)
    print("User Registerd Successfully!\n")


def login():
    username = str(input("Enter Your Name: "))
    password = str(input("Enter Your Password:"))


    hashed = hash_password(password)


    if user.get(username) == hashed:
        print("Login Successfull!\n")
    else:
        print("Invalid Credentials!\n")




while True:
    print("\n1. Sign Up")
    print("\n2. Log In")
    print("\n3. Exit\n")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        break
    else:
        print("Invalid Choice!\n")
        