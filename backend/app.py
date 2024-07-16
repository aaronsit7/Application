from flask import Flask, request, jsonify
from flask_cors import CORS
from login import login_user
from signup import create_user

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is running"

#code login and signup routes here


if __name__ == '__main__':
    app.run(debug=True)
