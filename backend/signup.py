import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

import pymongo
from pymongo import MongoClient
import bcrypt

# Connect to MongoDB
client = MongoClient("mongodb+srv://nisargbharucha:nisarg3903@cluster0.3rmhl7n.mongodb.net/")
db = client['login']
users_collection = db['shadlogin']

def create_user(username, password):
    # Check if the username already exists
    if users_collection.find_one({"username": username}):
        print("Username already exists. Please choose a different username.")
        return {"message": "Username already exists. Please choose a different username."}, 409

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create a new user document
    user_document = {
        "username": username,
        "password": hashed_password
    }

    # Insert the new user document into the collection
    users_collection.insert_one(user_document)
    print("User created successfully!")
    return {"message": "User created successfully!"}, 201


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_user(username, password)

if __name__ == "__main__":
    main()
