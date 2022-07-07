from webbrowser import get
from flask import Flask
from about import me
from data import mock_data
import json


app = Flask('server')

# app.run(port=5001)


@app.get('/')
def home():
    return "hello flask server!!"


@app.get('/test')
def test():
    return "this is just a simple test"


# @app.get('/about')
# def about():
#     return "Carlos Lopezz"


##############################################################
# API ENDPOINTS = PRODUCTS
##############################################################
@app.get('/api/version')
def version():
    return "1.0"

# get /api/about
# return first lastname


@app.get('/api/about')
def about():
    # return f'{me["first"]} {me["last"]}'
    return json.dumps(me)  # parse the dict into a json string


# - GET /api/products/<id> endpoint that returns the products with such id
@app.get("/api/products/<id>")
def get_products(id):
    for product in mock_data:
        if int(product["id"]) == int(id):
            print(product["id"])
            return json.dumps(product)
    return "Not found: " + id

# - GET /api/catalog endpoint that returns a list of products


@app.get('/api/products')
def catalog():
    return json.dumps(mock_data)

# - GET /api/catalog/cheapest returns the cheapest product on the list


@app.get('/api/products/cheapest')
def cheapproduct():
    minPrice = float(mock_data[0]["price"])
    mm = ""
    indexProduct = 0
    for product in mock_data:
        if float(product["price"]) < minPrice:
            minPrice = float(product["price"])
            indexProduct = product["id"]
    return get_products(indexProduct)

# - GET /api/catalog/total returns the total of adding up the products' prices


@app.get('/api/products/total')
def sum():
    sum = 0
    for product in mock_data:
        sum += float(product["price"])

    return json.dumps(sum)


app.run(debug=True)
