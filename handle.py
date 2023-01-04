from db import user_table, train_table

user_collection = user_table()

def authentication(username, password):
    for x in user_collection.find():
        if x['username'] == username and x['password'] == password:
            return True
    return False