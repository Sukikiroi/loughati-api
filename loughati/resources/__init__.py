from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
app.secret_key="secret ze3ma ze3ma"
CORS(app)