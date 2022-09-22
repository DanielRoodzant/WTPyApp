from flask import Flask
import numpy
import requests
#import daniel

# Hello World 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# API
app = Flask(__name__)

@app.route("/api")
def cats():
    cat =requests.get("https://catfact.ninja/facts")
    data = cat.json()
    fact = data["data"][numpy.random.choice(10)]
    return fact["fact"]
    
