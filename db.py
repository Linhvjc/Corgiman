from pymongo import MongoClient

# connect database
uri = 'mongodb://localhost:27017'
connection = MongoClient(uri)  

def train_table():
    # get table data
    return connection["chatbot"]["data_train"]

def user_table():
    return connection["chatbot"]["user"]

def message_table():
    return connection["chatbot"]["message"]

if __name__ == '__main__':
    print('db')