from http.client import responses

from flask import Flask, render_template,request,redirect
from pyexpat.errors import messages
import api

from db import Database

app = Flask(__name__)


dbo =Database()


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html', message="Registration successful. kindly login")
    else:
        return render_template('register.html', message="email already exits")

#         login mechanism        #
@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    respnse = dbo.search(email, password)
    if respnse:
        return redirect('/profile')
    else:
        return render_template('login.html', message="incorrect email/password")


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    print(response)
    return "Something"
app.run(debug=True)

