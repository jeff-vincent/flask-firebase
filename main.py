import json
from flask import Flask, request, render_template, send_file
import base_api


app = Flask(__name__, static_folder="public", template_folder="public")

@app.route('/', methods=['GET'])
def render_index():
    """
    Method for HTTP GET requests to "/"
    Returns index.
    Parameters:
        Request: The HTTP request.
        
    Returns:
        Rendered html: The index.html view.  
    """
    return render_template('index.html')

@app.route('/sign-up', methods=['POST'])
def sign_up():
    return base_api.sign_up(request)

@app.route('/log-in', methods=['POST'])
def log_in():
    return base_api.log_in(request)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
