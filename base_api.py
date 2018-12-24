import pyrebase

config = {
    "apiKey": "AIzaSyBN57Dy6pnMDAn1g4bs8oZsuRZtjjnanQg",
    "authDomain": "flask-firebase-49d67.firebaseapp.com",
    "databaseURL": "https://flask-firebase-49d67.firebaseio.com",
    "projectId": "flask-firebase-49d67",
    "storageBucket": "flask-firebase-49d67.appspot.com",
    "messagingSenderId": "103030528247"
}

firebase = pyrebase.initialize_app(config)

def sign_up(request):
    password = request.form.get('password')
    email = request.form.get('email')
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email, password)
    return user

def log_in(request):
    password = request.form.get('password')
    email = request.form.get('email')
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    return user