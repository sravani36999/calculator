import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="login_db"
)
cursor = conn.cursor()

while True:
    print("\n--- Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # -------- Register --------
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            print("Username already exists!")
        else:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)
            )
            conn.commit()
            print("Registration successful ✅")

    # -------- Login --------
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()

        if user:
            print("Login successful 🎉")
        else:
            print("Invalid username or password ❌")

    # -------- Exit --------
    elif choice == "3":
        print("Goodbye 😊")
        break

    else:
        print("Invalid choice!")

cursor.close()
conn.close()

