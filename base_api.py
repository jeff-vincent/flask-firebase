import pyrebase

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
}

firebase = pyrebase.initialize_app(config)

def log_in(request):
    password = request.form.get('password')
    email = request.form.get('email')
    auth = firebase.auth()
    #authenticate a user
    user = auth.sign_in_with_email_and_password(email, password)
    return user