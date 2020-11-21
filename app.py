from flask import Flask, render_template, request, session
import sqlite3
import os
from models import Account

app = Flask(__name__)
app.secret_key = 'hello world!'


@app.route('/')
def index():
    context = dict()
    return render_template('index.html', context = context)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    context = dict()

    if (session['user']):
        return render_template('my_account.html', context = context)


    if (request.method == 'GET'):
        return render_template('login.html', context = context)
    else:
        db_connection = sqlite3.connect('database.db')
        cursor = db_connection.cursor()

        login = request.form.get('login')
        password = request.form.get('password')

        cursor.execute('SELECT id, login, name FROM accounts WHERE login = ? AND password = ? ', [login,password])
        user = cursor.fetchone()
        
        if (user):
            session['user'] = {
            'id' : user[0],
            'login' : login,
            }
            return render_template('my_account.html', context = context)
        else:
            context['error_wrong_login'] = True
            return render_template('login.html', context = context)



        
        

        db_connection.commit()
        cursor.close()
        
        return render_template('login.html', context = context)
    

@app.route('/register', methods = ['POST', "GET"])
def register():
    context = dict()
    if (session['user']):
        return render_template('account.html', context = context)
    
    if (request.method == 'GET'):
        return render_template('registration.html', context = context)
    else:
        db_connection = sqlite3.connect('database.db')
        cursor = db_connection.cursor()
        
        login = request.form.get('login')
        name = request.form.get('name')
        password = request.form.get('password')

        cursor.execute('SELECT id, login, name FROM accounts WHERE login = ?', [login])
        result = cursor.fetchone()
        if (result):
            context['error_login_exists'] = True
            return render_template('registration.html', context = context)
        else:
            cursor.execute('SELECT COUNT(*) FROM accounts;')
            id = int(cursor.fetchone()[0])+1
            user = Account(id = id, login = login, name = name)
            session['user'] = {
                'id' : id,
                'login' : login,
                'name' : name
            }
            
            cursor.execute('INSERT INTO accounts (login, password, name) VALUES (?,?,?);', (user.login, password, user.name))
        
        
        db_connection.commit()
        cursor.close()
        return render_template('my_account.html', context = context)

@app.route('/exit')
def exit():
    context = dict()
    if (session['user']):
        session['user'] = None
        return render_template('index.html', context = context)
    else:
        return render_template('error.html', context = context)

@app.route('/all_users')
def all_users():
    context = dict()
    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM accounts;')
    users = cursor.fetchall()
    cursor.close()
    context['users'] = users
    return render_template('all_users.html', context = context)
    
@app.route('/my_account')
def my_account():
    context = dict()
    db_connection = sqlite3.connect('database.db')
   

    return render_template('all_users.html', context = context)

if __name__ == '__main__':
    app.run()
