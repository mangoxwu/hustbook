'''
@Description: 
@Author: wu xie
@Github: https://github.com/mangoxwu
@Date: 2019-06-12 21:32:01
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main/index.html")