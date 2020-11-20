from flask import Flask, render_template, request, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'hello world!'

# current_dir = os.path.dirname(os.path.abspath(__file__))
# db = sqlite3.connect("database.db")

@app.route('/')
def hello():
    context = dict()
    return render_template('index.html', context = context)

@app.route('/login')
def login():
    context = dict()
    return render_template('login.html', context = context)

@app.route('/register', methods = ['POST', "GET"])
def register():
    context = dict()
    if (request.method == 'GET'):
        return render_template('registration.html', context = context)
    else:
        
        login = request.form.get('login')
        name = request.form.get('name')
        password = request.form.get('password')
        session['user'] = name
        print(login, name, password)

        return render_template('account.html', context = context)

@app.route('/exit')
def exit():
    context = dict()
    if (session['user']):
        session['user'] = None
        return render_template('index.html', context = context)
    else:
        return render_template('error.html', context = context)


if __name__ == '__main__':
    app.run()
