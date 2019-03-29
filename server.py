# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request
from instaCrawl import *

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/post', methods=['POST'])

def post():
    choice1 = request.form['choice1']
    choice2 = request.form['choice2']
    result1 = crawl(choice1)
    result2 = crawl(choice2)
    result = result1 + result2
    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)