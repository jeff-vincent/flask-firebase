import pyrebase
from flask import jsonify

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
}

firebase = pyrebase.initialize_app(config)

def sign_up(request):
    password = request.form.get('password')
    email = request.form.get('email')
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email, password)
    return jsonify(user)

def log_in(request):
    password = request.form.get('password')
    email = request.form.get('email')
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    return jsonify(user)
