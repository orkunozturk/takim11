from flask import Flask, render_template, request
from hackathon.core import *

app = Flask(__name__)

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
 
@app.route('/')
def form():
    return render_template('General_Search_Results.html')
 
@app.route('/search', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        pass
        #text = request.form['stext']
        #processed_text = text.split(";")
        #return listToString(searchTextInFiles(processed_text))
    #return "<b>Hello World</b>"
    with open('content.txt', 'r') as file:
        data = file.read().replace('\n', '')
    return data
 
app.run(host='localhost', port=5000)
