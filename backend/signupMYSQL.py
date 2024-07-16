import mysql.connector
import bcrypt

# Connect to MySQL
db = mysql.connector.connect(
    host="shadlogin2.c5mvicgc5jsi.us-east-1.rds.amazonaws.com",
    user="admin",  # replace with your MySQL username
    password="admin123",  # replace with your MySQL password
    database="login"
)
cursor = db.cursor()

def create_user(username, password):
    # Debug print to check the input values
    print(f"Attempting to create user with username: '{username}'")

    if not username:
        print("Username cannot be empty.")
        return {"message": "Username cannot be empty."}, 400

    if not password:
        print("Password cannot be empty.")
        return {"message": "Password cannot be empty."}, 400

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user:
        print("Username already exists. Please choose a different username.")
        return {"message": "Username already exists. Please choose a different username."}, 409

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(f"Hashed password: {hashed_password}")

    # Create a new user
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        print("User created successfully!")
        return {"message": "User created successfully!"}, 201
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"message": f"Error: {err}"}, 500

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_user(username, password)

if __name__ == "__main__":
    main()
