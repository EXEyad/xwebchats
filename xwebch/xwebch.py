import csv
from flask import Flask, redirect, render_template, request, session, flash
from flask_session import Session
from werkzeug.security import generate_password_hash,check_password_hash
from cs50 import SQL

#Sign in Function
def sign_in(email,username,password):
    session['email'] = email
    session['username'] = username
    session['password'] = password

# Configure app
app = Flask(__name__)
app.secret_key = 'DEVCEYad'

# Configure db
db = SQL('sqlite:///users.db')
# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/",methods=['GET','POST'])
def index():
    if session['username']:
        return render_template("index.html", name=session['username'],mail=session["email"])
    else:
        return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Retrieve user data from the database by email
        user = db.execute("SELECT * FROM users WHERE email = ?", email)
        
        # Check if user exists and password is correct
        if len(user) == 1 and user[0]["password"] == password:
            flash("Login successful!")
            username = user[0]['username']
            sign_in(email,username,password)
            return redirect('/')
        else:
            flash("Invalid email or password!")
            return redirect("/login")
    else:
        return render_template("login.html")
    


@app.route("/logout")
def logout():
    session['username'] = None
    session['email'] = None
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")   
        user = db.execute('SELECT * FROM users WHERE email = ?',email)
        if len(user) == 1:
            return render_template('reg.html',MESSAGE='Email or Username Already Exists!')
        else:
            if '@xwbch.com' in email:
                db.execute("INSERT INTO users(email,password,username) VALUES (?,?,?) ", email,password,username)
                sign_in(email,username,password)
                return render_template('index.html',message='Registered Successfully.')
            else:
                return render_template('reg.html',MESSAGE='Email or Username Already Exists!')
    else:
        return render_template('reg.html')

@app.route('/account')
def account():
    if session['username']:
        hashed_password = generate_password_hash(session['password'])
        return render_template('acc.html',username=session['username'],email=session['email'],password= hashed_password )
    else:
        return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True, port=5000)