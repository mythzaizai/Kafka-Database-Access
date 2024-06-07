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
    
    return jsonify({"status": "User created successfully"}), 200


@app.route('/DB/UserID_Exist', methods=['GET'])
def UserID_Exist_route():

    user_id = request.args.get("UserID")
    
    if user_id is None:
        return jsonify({"status": "UserID not provided"}), 400
    
    exists = check_user_id_exist(user_id)
    result = {"exists": exists}

    return jsonify(result), 200


@app.route('/DB/Create_Chat', methods=['POST'])
def Create_Chat_route():

    ChatInfo = request.json

    print(ChatInfo)
    create_chat(ChatInfo)
    
    return jsonify({"status": "Chat created successfully"}), 200


@app.route('/DB/Update_ChatAmount', methods=['POST'])
def Update_ChatAmount_route():

    ChatInfo = request.json

    print(ChatInfo)
    update_chat_amount(ChatInfo)
    
    return jsonify({"status": "Update ChatAmount successfully"}), 200



@app.route('/DB/Group_Member_Exist', methods=['GET'])
def Group_Member_Exist_route():
    
    user_id = request.args.get("UserID")
    chat_id = request.args.get("ChatID")

    print(user_id)
    print(chat_id)
    
    if user_id is None or chat_id is None:
        return jsonify({"status": "UserID and ChatID are required"}), 400

    chat_relation = check_group_member_exist(user_id, chat_id)
    
    if chat_relation:
        return jsonify(chat_relation), 200
    else:
        return jsonify({"status": "Group member does not exist"}), 404


if __name__ == '__main__':
    app.run(port=8080)