from webbrowser import get
from flask import Flask


app = Flask('server')

# app.run(port=5001)


@app.get('/')
def home():
    return "hello flask server!!"


@app.get('/test')
def test():
    return "this is just a simple test"


@app.get('/about')
def about():
    return "Carlos Lopez"


##############################################################
# API ENDPOINTS = PRODUCTS
##############################################################
@app.get('/api/version')
def version():
    return "1.0"


app.run(debug=True)
