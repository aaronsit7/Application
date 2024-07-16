import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

import pymongo
from pymongo import MongoClient
import bcrypt

# Connect to MongoDB
client = MongoClient("mongodb+srv://nisargbharucha:nisarg3903@cluster0.3rmhl7n.mongodb.net/")
db = client['login']
users_collection = db['shadlogin']

def login_user(username, password):
    # Find the user by username
    user = users_collection.find_one({"username": username})
    if not user:
        print("Invalid username or password.")
        return {"message": "Invalid username or password."}, 401

    # Check the password
    if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        print("Invalid username or password.")
        return {"message": "Invalid username or password."}, 401
    print("Login successful!")
    return {"message": "Login successful!"}, 200


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_user(username, password)

if __name__ == "__main__":
    main()
