from db import user_table, train_table, message_table
from chatbot import chat
import time
from datetime import datetime

user_collection = user_table()
message_collection = message_table()
train_collection = train_table()

def authentication(username, password):
    for x in user_collection.find():
        if x['username'] == username and x['password'] == password:
            return True
    return False

def get_message_response(message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    response = chat(message)
    return dt_string, response

def store_message(username, client_message, bot_message, time):
    data = {
        "username": username,
        "client": client_message,
        "bot": bot_message,
        "time": time
    }
    message_collection.insert_one(data)
    
def get_message_database(username):
    return message_collection.find({"username": username})

def add_block_message(message, response):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return f"""
                            <div class="d-flex justify-content-end mb-4">
                                <div class="msg_cotainer_send">
                                    {message}
                                    <span class="msg_time_send">{dt_string}</span>
                                </div>
                                <div class="img_cont_msg">
                                    <img src="https://play-lh.googleusercontent.com/6f6MrwfRIEnR-OIKIt_O3VdplItbaMqtqgCNSOxcfVMCKGKsOdBK5XcI6HZpjssnB2Y"
                                        class="rounded-circle user_img_msg">
                                </div>
                            </div>;
                            <div class="d-flex justify-content-start mb-4">
                                <div class="img_cont_msg">
                                    <img src="https://static.turbosquid.com/Preview/001292/481/WV/_D.jpg" class="rounded-circle user_img_msg">
                                </div>
                                <div class="msg_cotainer">
                                    {response}
                                    <span class="msg_time">{dt_string}</span>
                                </div>
                            </div>
"""

def get_all_user_info():
    return user_collection.find()

def get_all_train_data():
    return train_collection.find()

if __name__ == '__main__':
    print('handle')