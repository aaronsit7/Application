import mysql.connector
import bcrypt

# Connect to MySQL
db = mysql.connector.connect(
    host="shadlogin2.c5mvicgc5jsi.us-east-1.rds.amazonaws.com",
    user="admin",   # replace with your MySQL username
    password="admin123",  # replace with your MySQL password
    database="login"
)
cursor = db.cursor()

def login_user(username, password):
    # Find the user by username
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        print("Invalid username or password.")
        return {"message": "Invalid username or password."}, 401

    # Check the password
    if not bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
        print("Invalid username or password.")
        return {"message": "Invalid username or password."}, 401

    print("Login successful!")
    return {"message": "Login successful!"}, 200




# Testing internal
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_user(username, password)

if __name__ == "__main__":
    main()
