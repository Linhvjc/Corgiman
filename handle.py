from db import user_table, train_table, message_table, message_no_response_table
from chatbot import chat
import time
from datetime import datetime

user_collection = user_table()
message_collection = message_table()
train_collection = train_table()
message_no_response_collection = message_no_response_table()

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

def get_all_tag():
    result = []
    for x in train_collection.find():
        result.append(x['tag'])
    return result

all_response_noanswer = train_collection.find_one({'tag': 'noanswer'})['responses']

def check_if_message_in_noanswer(message):
    if message in all_response_noanswer:
        return True
    else:
        return False

def get_all_message_no_response_data():
    return message_no_response_collection.find()

def all_tag_option():
    result = ''
    for x in train_collection.find():
        result += f'''<option value="{ x['tag'] }"> { x['tag'] } </option>'''
    return result

def add_pattern(tag, new_pattern):
    all_pattern = train_collection.find_one({'tag': tag})['patterns']
    all_pattern = str(all_pattern)
    if len(all_pattern) >2:
        all_pattern = all_pattern.replace('"', "'")
        all_pattern = all_pattern[2:-2]
        new_arr = all_pattern.split("', '")
        new_arr.append(new_pattern)
    else:
        new_arr = [new_pattern]
    train_collection.update_one({"tag": tag}, {"$set": {"patterns": new_arr}})

def remove_pattern(tag, pattern_delete):
    all_pattern = train_collection.find_one({'tag': tag})['patterns']
    all_pattern = str(all_pattern)
    all_pattern = all_pattern.replace('"', "'")
    all_pattern = all_pattern[2:-2]
    
    new_arr = all_pattern.split("', '")
    new_arr.remove(pattern_delete)
    
    train_collection.update_one({"tag": tag}, {"$set": {"patterns": new_arr}})
    
def add_response(tag, new_response):
    all_response = train_collection.find_one({'tag': tag})['responses']
    all_response = str(all_response)
    if len(all_response) >2:
        all_response = all_response.replace('"', "'")
        all_response = all_response[2:-2]
        new_arr = all_response.split("', '")
        new_arr.append(new_response)
    else:
        new_arr = [new_response]
    train_collection.update_one({"tag": tag}, {"$set": {"responses": new_arr}})    
    
def remove_response(tag, response_delete):
    all_response = train_collection.find_one({'tag': tag})['responses']
    all_response = str(all_response)
    all_response = all_response.replace('"', "'")
    all_response = all_response[2:-2]
    
    new_arr = all_response.split("', '")
    new_arr.remove(response_delete)
    
    train_collection.update_one({"tag": tag}, {"$set": {"responses": new_arr}})
    
if __name__ == '__main__':
    print()