users = {}

while True:
    print("\n--- Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        if username in users:
            print("Username already exists!")
        else:
            users[username] = password
            print("Registration successful")

    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter Password: ")
        if username in users:
            if users[username] == password:
                print("Login successfull")
            else:
                print("Wrong Password")
        else:
            print("Invalid Credentials!")

    elif choice == 3:
        print("Bye !!!")
        break
    
    else:
        print("Invalid Choice!!")


