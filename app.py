#Step 1: Create a new Flask app instance

from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

# Step 2: Define the routes used for login and sign-up pages and create new .html files for login/sign-up pages

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = {}

        try:
            with open('users.json', 'r') as data_file:
                data = json.load(data_file)
        except:
            data = {}

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        users[username] = {'password': password, 'email': email}
        data.update(users)

        with open('users.json', 'w') as data_file:
            json.dump(data, data_file)

        session['username'] = username

        return redirect(url_for('home'))

    return render_template('register.html')

# Step 3: Create new .css files for login/sign-up pages 

# Step 4: Add code for basic functionality to the routes

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Step 5: Create a session variable for the user after the sign-in is successful.

session['username'] = username

# Step 6: Implement Logout functionality

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Step 7: Create the necessary Python methods to handle form submissions, add validation checks and store valid user details in the local JSON file.

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = {}

        try:
            with open('users.json', 'r') as data_file:
                data = json.load(data_file)
        except:
            data = {}

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        if username in data:
           return 'Username already taken'

        if not username.isalnum():
            return 'Username must be alphanumeric'
        
        if len(password)<4:
            return 'Password must be at least 4 digits'


        users[username] = {'password': password, 'email': email}
        data.update(users)

        with open('users.json', 'w') as data_file:
            json.dump(data, data_file)

        session['username'] = username

        return redirect(url_for('home'))

    return render_template('register.html')


# Step 8: Create the routes for sign up and login forms. Process incoming form data and store it in our local JSON database. Authenticate existing users when they log in through a Flask session.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with open('users.json', 'r') as data_file:
                data = json.load(data_file)
        except:
            data = {}

        if username in data:
            if password == data[username]['password']:
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return 'Invalid username or password'
        else:
            return 'Invalid username or password'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = {}

        try:
            with open('users.json', 'r') as data_file:
                data = json.load(data_file)
        except:
            data = {}

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if username in data:
            return 'Username already taken'

        if not username.isalnum():
            return 'Username must be alphanumeric'

        if len(password)<4:
            return 'Password must be at least 4 digits'
            
        users[username] = {'password': password, 'email': email}
        data.update(users)

        with open('users.json', 'w') as data_file:
            json.dump(data, data_file)

        session['username'] = username

        return redirect(url_for('home'))

    return render_template('register.html')


