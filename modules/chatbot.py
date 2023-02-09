import random
import pickle
import numpy as np
import os

# connect database
from db import train_table

import nltk
from nltk.stem import WordNetLemmatizer     #verify the same word
from keras.models import load_model


# get data from database
train_collection = train_table()

current_path = os.getcwd()
lemmatizer = WordNetLemmatizer()       #verify the same word

# Load data is trained
words = pickle.load(open(current_path+'/data/words.pkl', 'rb'))     
classes = pickle.load(open(current_path+'/data/classes.pkl', 'rb'))
model = load_model(current_path+'/data/chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)   # split sentence to array
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]    # check if same word
    return sentence_words

def bag_of_word(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)          #[0,0,0,...,0]      Size = len(words)
    for w in sentence_words:
        for i, word in enumerate(words):        # enumerate: ['a', 'b', 'c'] => [ (0,'a'), (1,'b'), (2,'c')]
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_word(sentence)
    res = model.predict(np.array([bow]))[0];
    # print("res: " + str(res)) # Prediction rate
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i,r in enumerate(res) if r > ERROR_THRESHOLD] # => result = the value > 0.25
    results.sort(key = lambda x: x[1], reverse=True) # get the highest value [[2, 0.9970567]]
    # print("results: " + str(results))
    return_list = []
    # check meaningful sentences
    if len(results) == 0:
        return_list = [{'intent': 'no answer'}]
    elif results[0][1] < 0.6:
        return_list = [{'intent': 'no answer'}]
    else:
        for r in results:
            return_list.append({'intent': classes[r[0]], 'probability': str(r[1])}) # r[0] is index, r[1] is value.
            # example: [{'intent': 'greetings', 'probability': '0.9970567'}]
    return return_list      # result list

def get_response(intents_list, intents_json):
    # get the first value ( the value has probability highest)
    tag = intents_list[0]['intent']
    for intent in intents_json:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I can't get it"

# print("Go! Bot is running")

def chat(message):
    # predict class
    ints = predict_class(message)
    # get response
    res = get_response(ints, train_collection.find())
    print("Bot: " + res)
    return res

if __name__ == '__main__':
    chat(input(''))