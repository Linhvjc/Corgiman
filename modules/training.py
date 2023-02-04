import random
import os
import json
import pickle       # for serialization
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer     #verify the same word
# connect database
from modules.db import train_table

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.optimizers import gradient_descent_v2

def training_data_database():

    # get data from database
    train_collection = train_table()

    current_path = os.getcwd()
    lemmatizer = WordNetLemmatizer()        #verify the same word


    words = []          # All the words
    classes = []        # All class 
    documents = []      # all word with tag
    ignore_letters = ['?', '!', '.', ',']       # all ignore letters


    # loop throw item in intents
    for intent in train_collection.find():
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)  # it look like split function ( 'what your name' => ['what', 'your','name'] )
            words.extend(word_list)     # add to array words
            documents.append((word_list, intent['tag']))   # add all word with tag to array documents
            if intent['tag'] not in classes:
                classes.append(intent['tag'])       # check if tag already have in classes and then add to array classes

    words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]        # remove ignore letter and same word
    words = sorted(set(words))          # Sort

    classes = sorted(set(classes))      # Sort

    pickle.dump(words, open(current_path+'/data/words.pkl', 'wb'))      # Write word to file .pkl
    pickle.dump(classes, open(current_path+'/data/classes.pkl', 'wb'))  # Write classes to file .pkl

    training = []       # data to train
    output_empty = [0] * len(classes)       # Array contain the number of elements is 0 equal to len(classes)

    # loop throw item in documents
    for document in documents:
        bag = []
        word_patterns = document[0]         # list word
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]      # lowercase 
        # loop throw word in words list
        for word in words:          
            bag.append(1) if word in word_patterns else bag.append(0)           # check if word exist in words

        output_row = list(output_empty)  # [0,0,0,...,0]
        output_row[classes.index(document[1])] = 1          # get index of intent
        training.append([bag, output_row])      # add to data
    random.shuffle(training)        # shuffle data
    training = np.array(training)   # Convert to numpy array    

    train_x = list(training[:,0])      # X train
    train_y = list(training[:,1])       # y train

    # Create model (Dense neural network)
    model = Sequential()
    model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))     # limit overfitting
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))     # limit overfitting
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))     # limit overfitting
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # optimizer
    sgd = gradient_descent_v2.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    # fit and save history
    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=10, verbose=1)   # training
    model.save(current_path+'/data/chatbot_model.h5', hist)     # Save model
    
def training_data_json():
    lemmatizer = WordNetLemmatizer()        #verify the same word

    intents = json.loads(open('./data/intents.json').read())       #Load file json

    words = []          # All the words
    classes = []        # All class 
    documents = []
    ignore_letters = ['?', '!', '.', ',']       # all ignore letters

    for intent in intents["intents"]:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)  # it look like split function ( 'what your name' => ['what', 'your','name'] )
            words.extend(word_list)     # add to array words
            documents.append((word_list, intent['tag']))   # add all word with tag to array documents
            if intent['tag'] not in classes:
                classes.append(intent['tag'])       # check if tag already have in classes and then add to array classes

    words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
    words = sorted(set(words))

    classes = sorted(set(classes))

    pickle.dump(words, open('./data/words.pkl', 'wb'))
    pickle.dump(classes, open('./data/classes.pkl', 'wb'))

    training = []
    output_empty = [0] * len(classes)

    for document in documents:
        bag = []
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
        training.append([bag, output_row])
    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:,0])
    train_y = list(training[:,1])

    model = Sequential()
    model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))     # limit overfitting
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))     # limit overfitting
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))     # limit overfitting
    model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = gradient_descent_v2.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    # fit and save history
    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=10, verbose=1)
    model.save('./data/chatbot_model.h5', hist)
if __name__ == '__main__':
    training_data_database()
