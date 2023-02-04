# import
from flask import Flask, render_template, request, session, redirect, url_for
from modules.db import user_table, train_table, message_no_response_table, message_table
from modules.handle import authentication,add_json_data_to_database,check_username_exist, add_pattern, remove_pattern,add_response,remove_response, all_tag_option, check_if_message_in_noanswer, get_all_message_no_response_data, get_message_response, store_message, get_message_database, add_block_message, get_all_user_info, get_all_train_data
from modules.training import training_data_database, training_data_json
from datetime import datetime
from flask_socketio import SocketIO, send

#! Create app and socket
app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "linhphan"
socketio = SocketIO(app, cors_allowed_origins='*')

#! Get data from database
user_collection = user_table()
train_collection = train_table()
message_collection = message_table()
message_no_response_collection = message_no_response_table()

#! send message realtime
@socketio.on('message')
def handle_message(message):
    message = message.strip()
    if message != "User connected!":
        if message != "":
            # Get response and time
            curr_time, response = get_message_response(message)
            # Check response if in table noanswer
            if check_if_message_in_noanswer(response): 
                # insert to new table for admin answer
                message_no_response_collection.insert_one({"message": message})
            # Get HTML code
            data_response = add_block_message(message, response)
            # Save history
            store_message(session['username'], message, response, curr_time)
            # Send message
            send(data_response, broadcast=True)
    else:
        send(message, broadcast=True)
        
#! Error page
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

#! Main route
@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "GET":
        # Check if username and password in session
        if 'username' in session and 'password' in session:
            message_data = get_message_database(session['username'])
            total_messages = message_collection.count_documents({"username": session['username']})
            return render_template('main.html', data = message_data, 
                                   username = session['username'], message_quantity = total_messages*2)
        else:
            return redirect(url_for("login"))

#! login route
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # get username and password from form
        username = request.form['username']
        password = request.form['password']
        # check authenticator
        if authentication(username, password):
            # get date time
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            # update last login
            user_collection.update_one({"username": username}, {"$set": {"last_login": dt_string}})
            # Save to session
            session['username'] = username
            session['password'] = password
            # check the role of user
            if username == 'admin':
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("main"))
        else:
            return render_template('auth/login.html', message = 'Wrong username or password')
    else:
        # check if login
        if 'username' in session and 'password' in session:
            message_data = get_message_database(session['username'])
            return render_template('main.html', data = message_data)
        else:
            return render_template('auth/login.html', message = '')
    
#! logout route
@app.route('/logout', methods=["POST", "GET"])
def logout():
    # clear session and redirect to login page
    session.clear()
    return redirect(url_for("login"))

#! Register route
@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # Get data from form register
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        if check_username_exist(username):
            return render_template('auth/register.html', message = 'Username has already exist!')
        elif len(password) < 6 :
            return render_template('auth/register.html', message = 'Password must be more than 6 characters!')
        elif confirm_password != password:
            return render_template('auth/register.html', message = 'Wrong confirm password!')
        else:
            # insert data to database
            user_collection.insert_one({
                "username": username,
                "password": password,
                "last_login": ""
            })
            return redirect(url_for("login"))
    else:
        return render_template('auth/register.html', message = '')

#! Admin route
@app.get('/admin')
def admin():
    # check if admin
    if 'username' not in session or 'password' not in session:
        return redirect(url_for("login"))
    elif session['username'] != 'admin':
        return redirect(url_for("main"))
    else:
        return render_template('admin.html', user_data = get_all_user_info(), train_data = get_all_train_data(), 
                               message_to_answer_data = get_all_message_no_response_data(), tag_data = all_tag_option())

@app.post('/admin')
def admin_action():
    # USER SECTION
    if "delete_user" in request.form: 
        delete_user = request.form['delete_user']
        user_collection.delete_one({"username": delete_user})
        message_collection.delete_many({"username": delete_user})
    
    # TRAIN SECTION
    if "add_tag" in request.form: 
        new_tag = request.form['add_tag']
        train_collection.insert_one({
            'tag': new_tag,
            'patterns': [],
            'responses': []
        })
    if "delete_tag" in request.form:
        delete_tag = request.form['delete_tag']
        train_collection.delete_one({"tag" : delete_tag})
    if "add_pattern" in request.form:
        new_pattern = request.form['add_pattern']
        tag = request.form['tag_to_add_pattern']
        add_pattern(tag,new_pattern)
    if "delete_pattern" in request.form:
        result = request.form['delete_pattern']
        [pattern_delete, tag] = result.split(';_;')
        remove_pattern(tag, pattern_delete)
        
    if "add_response" in request.form:
        new_response = request.form['add_response']
        tag = request.form['tag_to_add_response']
        add_response(tag,new_response)
    if "delete_response" in request.form:
        result = request.form['delete_response']
        [response_delete, tag] = result.split(';_;')
        remove_response(tag, response_delete)
    if "training" in request.form:
        total_train_documents = train_collection.count_documents({})
        if total_train_documents > 0:
            training_data_database()
        else:
            training_data_json()
            add_json_data_to_database()
    # MESSAGE TO RESPONSE SECTION
    if "btn_add_message_to_answer" in request.form:
        message_to_response = request.form['btn_add_message_to_answer']
        tag_to_add = request.form['tag_message_to_answer']
        add_pattern(tag_to_add, message_to_response)
        message_no_response_collection.delete_one({"message": message_to_response})
    if "btn_delete_message_to_answer" in request.form:
        message_to_response = request.form['btn_delete_message_to_answer']
        message_no_response_collection.delete_one({"message": message_to_response})
        
    
    return redirect(url_for("admin"))


if __name__ == '__main__':
    socketio.run(app, host="localhost")