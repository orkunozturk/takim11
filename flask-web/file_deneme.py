#flask app to display pdf on the browser
from flask import Flask, send_from_directory
import os
 
app = Flask(__name__)
 
@app.route("/")
def tos():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/files/'
    return send_from_directory(filepath, 'tos.pdf')
