from flask import Flask, render_template, request, session, get_template_attribute, redirect, url_for, jsonify, stream_template 
from markupsafe import escape
from db import user_table, train_table
from handle import authentication, get_message_response, store_message, get_message_database, add_block_message
from chatbot import chat
import time
from flask_socketio import SocketIO, send

app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "linhphan"
socketio = SocketIO(app, cors_allowed_origins='*')

# Get data from database
user_collection = user_table()

# send message realtime
@socketio.on('message')
def handle_message(message):
    message = message.strip()
    if message != "User connected!":
        if message != "":
            curr_time, response = get_message_response(message)
            data_response = add_block_message(message, response)
            store_message(session['username'], message, response, curr_time)
            send(data_response, broadcast=True)
    else:
        send(message, broadcast=True)

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "GET":
        if 'username' in session and 'password' in session:
            message_data = get_message_database(session['username'])
            return render_template('main.html', data = message_data)
        else:
            return redirect(url_for("login"))

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if authentication(username, password):
            session['message'] = ''
            session['username'] = username
            session['password'] = password
            return redirect(url_for("main"))
        else:
            return render_template('auth/login.html', message = 'Wrong username or password')
    else:
        if 'username' in session and 'password' in session:
            message_data = get_message_database(session['username'])
            return render_template('main.html', data = message_data)
        else:
            return render_template('auth/login.html', message = '')
    
    
@app.route('/logout', methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        user_collection.insert_one({
            "username": username,
            "password": password
        })
        return redirect(url_for("login"))
    else:
        return render_template('auth/register.html')
    

if __name__ == '__main__':
    socketio.run(app, host="localhost")