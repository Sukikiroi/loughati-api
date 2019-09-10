"""
init file
"""
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from .views import app


@app.cli.command()
def run_migration():
    pass
@app.cli.command()
def init_db():
    pass