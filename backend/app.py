from flask import Flask, request, jsonify
from flask_cors import CORS
from login import login_user
from signup import create_user

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is running"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    result, status_code = login_user(username, password)
    return jsonify(result), status_code


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    result, status_code = create_user(username, password)
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True)
