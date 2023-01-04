from flask import Flask, render_template, request, session
from markupsafe import escape
from flask import request, redirect, url_for
from db import user_table, train_table
from handle import authentication

app = Flask(__name__)
app.config["SECRET_KEY"] = "linhphan"

# Get data from database
user_collection = user_table()

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "GET":
        if 'username' in session and 'password' in session:
                return render_template('main.html')
        else:
            return redirect(url_for("login"))
    

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if authentication(username, password):
            session['username'] = username
            session['password'] = password
            return redirect(url_for("main"))
        else:
            return render_template('auth/login.html', message = 'Wrong username or password')
    else:
        if 'username' in session and 'password' in session:
            return render_template('main.html')
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