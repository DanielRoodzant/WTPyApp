from flask import Flask
import numpy
import requests
import pandas as pd
#import daniel

# Hello World 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# API
@app.route("/api")
def cats():
    cat =requests.get("https://catfact.ninja/facts")
    data = cat.json()
    fact = data["data"][numpy.random.choice(10)]
    return fact["fact"]

#CSV
@app.route("/csv")
def pokemon():
    df=pd.read_csv("Pokemon.csv")
    namen = df.sample()
    return (namen.to_string())
    
    
