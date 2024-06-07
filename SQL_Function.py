import sqlite3

# Create a new user with UserInfo
def create_user(UserInfo):

    user_tuple = (
        UserInfo["UserID"],
        UserInfo["UserName"],
        UserInfo["Account"],
        UserInfo["Password"],
        UserInfo["Avatar"],
        UserInfo["PersonalInfo"],
        UserInfo["Status"]
    )
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (UserID, UserName, Account, Password, Avatar, PersonalInfo, Status) VALUES (?, ?, ?, ?, ?, ?, ?)", user_tuple)
    
    conn.commit()
    conn.close()

# Check if UserID exists
def check_user_id_exist(UserID):

  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM Users WHERE UserID=?", (UserID,))
  result = cursor.fetchone()[0]
  conn.close()

  return result > 0


# Create a new chat with ChatInfo and ChatRelation
def create_chat(ChatInfo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # 插入到 Chats 表
    chat_tuple = (
        ChatInfo["ChatID"],
        ChatInfo["ChatName"],
        ChatInfo["Amount"]
    )
    cursor.execute("INSERT INTO Chats (ChatID, ChatName, ChatAmount) VALUES (?, ?, ?)", chat_tuple)
    
    # 插入到 ChatRelations 表
    chat_relation_tuple = (
        ChatInfo["ChatRelation"]["ChatID"],
        ChatInfo["ChatRelation"]["UserID"],
        ChatInfo["ChatRelation"]["UserAuthority"]
    )
    cursor.execute("INSERT INTO ChatRelations (ChatID, UserID, UserAuthority) VALUES (?, ?, ?)", chat_relation_tuple)
    
    conn.commit()
    conn.close()



# Update ChatAmount
def update_chat_amount(ChatInfo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Chats SET ChatAmount = ? WHERE ChatID = ?", (ChatInfo["Amount"], ChatInfo["ChatID"]))
    
    conn.commit()
    conn.close()




# Check if the user is in the group
def check_group_member_exist(UserID, ChatID):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT ROWID, ChatID, UserID, UserAuthority FROM ChatRelations WHERE UserID=? AND ChatID=?", (UserID, ChatID))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {
            "UserAuthority": result[0],
            "UserID": result[1],
            "ChatID": result[2]
        }
    else:
        return None
