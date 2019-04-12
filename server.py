# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request
from instaCrawl import *
from googleTrend import *
from choose import *
import random

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    choice1 = request.form['choice1']
    choice2 = request.form['choice2']
    #result1 = instaCrawl(choice1)
    #result2 = instaCrawl(choice2)
    #result = result1 + result2
    #print(result)
    #choose(choice1, choice2)
    r = round(random.random(),2)
    if r > 0.5:
        result=choice1
    else:
        result = choice2
    return render_template('loading.html', decision = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)