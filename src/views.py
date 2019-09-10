"""
Views File where all routes will be
Might Add an Api file for more readability 
"""
from flask import render_template
from .model import app

@app.route("/")
def index():
    return "shlada"