import pyrebase

config = {
    "apiKey": "AIzaSyCVQZxTHUb1loEoUQdcXBAz4DkyGQOFFB0",
    "authDomain": "flask-firebase-b6952.firebaseapp.com",
    "databaseURL": "https://flask-firebase-b6952.firebaseio.com",
    "projectId": "flask-firebase-b6952",
    "storageBucket": "flask-firebase-b6952.appspot.com",
    "messagingSenderId": "218539348402"
}

firebase = pyrebase.initialize_app(config)

def sign_up(request):
    password = request.args.get('password')
    email = request.args.get('email')
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email, password)
    return user

def log_in(request):
    password = request.args.get('password')
    email = request.args.get('email')
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    return user