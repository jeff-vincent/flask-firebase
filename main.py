import requests
from flask import Flask, request, render_template

app = Flask(__name__, static_folder="public", template_folder="public")

@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')

@app.route('/signUp', methods=['POST'])
def sign_up():
    print('post works')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
