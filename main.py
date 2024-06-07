from flask import Flask, request, jsonify
import sqlite3
import os
from SQL_Function import *
from init_DB import init_db

app = Flask(__name__)

# Database setup

if not os.path.exists('database.db'):
    init_db()

# Routes
@app.route('/DB/Create_User', methods=['POST'])
def create_user_route():

    UserInfo = request.json

    print(UserInfo)
    create_user(UserInfo)
    
    return jsonify({"status": "User created successfully"}), 201

@app.route('/DB/UserID_Exist', methods=['POST'])
def UserID_Exist_route():

    UserInfo = request.json
    print(UserInfo)

    return jsonify({"status": "UserID_Exist"}), 201

if __name__ == '__main__':
    app.run(port=8080)