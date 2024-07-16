import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="shadlogin2.c5mvicgc5jsi.us-east-1.rds.amazonaws.com",
    user="admin",  # replace with your MySQL username
    password="admin123",  # replace with your MySQL password
    database="login"
)
cursor = db.cursor()

def fetch_all_users():
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        if rows:
            print("Users in the database:")
            for row in rows:
                print(row)
        else:
            print("No users found in the database.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    fetch_all_users()

if __name__ == "__main__":
    main()
