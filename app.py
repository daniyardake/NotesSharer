from flask import Flask, render_template, request, session
import sqlite3
import os
from models import Account

app = Flask(__name__)
app.secret_key = 'hello world!'


@app.route('/')
def index():
    context = dict()
    context['main'] = True


    
    return render_template('index.html', context = context)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    context = dict()
    


    # if (session['user']):
    #     return render_template('my_account.html', context = context)
    if (request.method == 'GET'):
        return render_template('login.html', context = context)
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        try:
            db_connection = sqlite3.connect('database.db')
            cursor = db_connection.cursor()
            cursor.execute('SELECT id, login, name FROM accounts WHERE login = ? AND password = ? ', [login,password])
            user = cursor.fetchone()
        except:
            print('DATABASE EROOR!!!!!!!!')
        

        
        if (user):
            session['user'] = {
            'id' : user[0],
            'login' : login,
            }
            return notes()
        else:
            context['error_wrong_login'] = True
            return render_template('login.html', context = context)



        
        

        db_connection.commit()
        cursor.close()
        
        return render_template('login.html', context = context)
    
@app.route('/register', methods = ['POST', "GET"])
def register():
    context = dict()
    

    
    if (request.method == 'GET'):
        return render_template('registration.html', context = context)
    else:
        db_connection = sqlite3.connect('database.db')
        cursor = db_connection.cursor()
        
        login = request.form.get('login')
        name = request.form.get('name')
        password = request.form.get('password')
        university = request.form.get('university')
        github = request.form.get('github')

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
            
            cursor.execute('INSERT INTO accounts (login, password, name, university, github) VALUES (?,?,?,?,?);', (user.login, password, user.name, university, github))
        
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

@app.route('/users')
def all_users():
    if (not session['user']):
        return render_template('404.html', error = 'You are not loged in to view this page')
    context = dict()
    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM accounts;')
    users = cursor.fetchall()
    cursor.close()
    context['users'] = users
    return render_template('all_users.html', context = context)
    
@app.route('/users/<login>')
def user(login):
    context = dict()
    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT accounts.login, accounts.id, accounts.name, accounts.github, accounts.university FROM accounts WHERE accounts.login=?', [login])
    user = cursor.fetchone()
    context['user'] = user

    cursor.execute('SELECT notes.content, notes.class, notes.lectureName, notes.university, notes.noteID FROM notes WHERE notes.author=?', [user[1]])
    notes = cursor.fetchall()
    context['notes'] = notes

    return render_template('profile.html', context = context)


@app.route('/my_account')
def my_account():
    context = dict()

    #context['login'] = session['user']['login']
    return render_template('my_account.html', context = context)

@app.route('/notes', methods = ['GET', 'POST'])
def notes():
    if (not session['user']):
        return render_template('404.html', error = 'You are not loged in to view this page')

        

    context = dict()

    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()

    if (request.method == 'POST'):
        search = request.form.get('searchQ')
        type_search = request.form.get('type')
        
        
        if (type_search == 'University'):
            cursor.execute('SELECT * FROM notes WHERE instr(?,notes.university)>0;', [search])
        elif (type_search == 'Class'):
            cursor.execute('SELECT * FROM notes WHERE instr(?,notes.class)>0;', [search])
        elif (type_search == 'Content'):
            cursor.execute('SELECT * FROM notes WHERE instr(?,notes.content)>0;', [search])
        elif (type_search == 'Author'):
            cursor.execute('SELECT * FROM notes INNER JOIN accounts ON notes.author = accounts.id WHERE instr(?,accounts.login)>0;', [search])
        else:
            cursor.execute('SELECT * FROM notes;')
        
        notes = cursor.fetchall()
        cursor.close()
        context['notes'] = reversed(notes)

    else:
        cursor.execute('SELECT * FROM notes;')
        notes = cursor.fetchall()
        cursor.close()
        context['notes'] = reversed(notes)
    return render_template('notes.html', context = context)

@app.route('/notes/<id>', methods = ['POST', 'GET'])
def note(id):
    if (not session['user']):
        return render_template('404.html', error = 'You are not loged in to view this page')
    context = dict()
    
    db_connection = sqlite3.connect('database.db')
    if (request.method == 'POST'):
        comment = request.form.get('comment')
        cursor = db_connection.cursor()
        cursor.execute('INSERT INTO comments (content, author, note) VALUES (?,?,?);', (comment, session['user']['id'], id))
        db_connection.commit()
        cursor.close()
 
    cursor = db_connection.cursor()
    cursor.execute('SELECT notes.content,  notes.university, notes.class, notes.lectureName, accounts.login, notes.noteID FROM notes INNER JOIN accounts ON notes.author = accounts.id WHERE notes.noteID = ? ', [id])
    note = cursor.fetchone()
    context['note'] = note

    cursor.execute('SELECT comments.content, accounts.login FROM comments INNER JOIN accounts ON comments.author=accounts.id WHERE comments.note=?;', [id])
    comments = cursor.fetchall()
    context['comments'] = comments



    return render_template('note.html', context = context)


@app.route('/notes/add', methods = ['POST', 'GET'])
def add_note():
    if (not session['user']):
        return render_template('404.html', error = 'You are not loged in to view this page')
    context = dict()
    if request.method == 'POST':
        university = request.form.get('university')
        cl = request.form.get('class')
        name = request.form.get('name')
        content = request.form.get('content')
        db_connection = sqlite3.connect('database.db')
        cursor = db_connection.cursor()
        cursor.execute('INSERT INTO notes (content, author, university, class, lectureName) VALUES (?,?,?,?,?);', (content, session['user']['id'], university, cl, name))
        db_connection.commit()
        cursor.close()
        

    return render_template('add_note.html', context = context)

@app.route('/notes/<id>/edit', methods = ['POST', 'GET'])
def edit_note(id):
    if (not session['user']):
        return render_template('404.html', error = 'You are not loged in to view this page')
    context = dict()
    
    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT notes.content, notes.university, notes.lectureName, notes.author, notes.class FROM notes WHERE notes.noteID = ?', [id])
    note = cursor.fetchone()
    context['note'] = note

    if (not note[3]==session['user']['id']):
        return render_template('404.html', error = 'You are not alowed to edit this note')
    

    if request.method == 'POST':
        university = request.form.get('university')
        cl = request.form.get('class')
        name = request.form.get('name')
        content = request.form.get('content')
        cursor = db_connection.cursor()
        cursor.execute('UPDATE notes SET content = ?, university = ?, class = ?, lectureName = ? WHERE notes.noteID = ?', (content, university, cl, name,id))
        db_connection.commit()
        cursor.close()
        
        return render_template('edit_note.html', context = context)

        

    return render_template('edit_note.html', context = context)

@app.route('/users/<login>/edit', methods = ['POST', 'GET'])
def edit_user(login):
    if (not session['user']):
        return render_template('404.html', error = 'You are not loged in to view this page')
    context = dict()
    
    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT accounts.name, accounts.university, accounts.github FROM accounts WHERE accounts.login = ?', [login])
    user = cursor.fetchone()
    context['user'] = user

    if (not login==session['user']['login']):
        return render_template('404.html', error = 'You are not alowed to edit this user')
    

    if request.method == 'POST':
        
        name = request.form.get('name')
        university = request.form.get('university')
        github = request.form.get('github')

        
        cursor = db_connection.cursor()
        cursor.execute('UPDATE accounts SET name = ?, university = ?, github = ? WHERE accounts.login = ?', (name, university, github, login))
        db_connection.commit()
        cursor.close()
        
        return render_template('edit_account.html', context = context)

        

    return render_template('edit_account.html', context = context)
if __name__ == '__main__':
    
    app.run()