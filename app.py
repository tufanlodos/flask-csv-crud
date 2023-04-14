"""
To run (after environment setup):
(env) $ python -m pip install -r requirements.txt
(env) $ FLASK_DEBUG=True python -m flask run
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'
