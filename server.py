from flask import Flask
from unittest import mock
from webbrowser import get
from about import me
from data import mock_data
import json


app = Flask('server')


@app.get('/')
def home():
    return "hello flask server: Organika!!"


@app.get('/test')
def test():
    return "this is just a simple test"


##############################################################
# API ENDPOINTS = PRODUCTS
##############################################################
@app.get('/api/version')
def version():
    return "1.0"

# get /api/about  return first lastname


@app.get('/api/about')
def about():
    # return f'{me["first"]} {me["last"]}'
    return json.dumps(me)  # parse the dict into a json string

# - GET /api/catalog endpoint that returns a list of products


@app.get('/api/products')
def catalog():
    return json.dumps(mock_data)

# - GET /api/products/<id> endpoint that returns the products with such id


@app.get("/api/products/<id>")
def get_products(id):
    for product in mock_data:
        if int(product["id"]) == int(id):
            print(product["id"])
            return json.dumps(product)
    return "Not found: " + id


# - GET /api/catalog/cheapest returns the cheapest product on the list
@app.get('/api/product_cheapest')
def cheapproduct():
    minPrice = mock_data[0]
    for product in mock_data:
        if product["price"] < minPrice["price"]:
            minPrice = product
    return json.dumps(minPrice)


# - GET /api/catalog/expensive returns the most expensive product on the list
@app.get('/api/products_expensive')
def expensiveProduct():
    maxPrice =mock_data[0]
    for product in mock_data:
        if product["price"] > maxPrice["price"]:
            maxPrice = product
    return json.dumps(maxPrice)

# - GET /api/catalog/total returns the total of adding up the products' prices


@app.get('/api/products/total')
def sum():
    sum = 0
    for product in mock_data:
        sum += float(product["price"])
    return json.dumps(sum)

# create a results list
# travel the list, get every prod
# if prod -> category is equal to the category variable
# add prod to the results list
# outside the for loop, return the results list as json


#GET /api/catalog/<category> returns the products that belongs to a specified category
@app.get("/api/products_category/<cat>")
def listByCategory(cat):
    listProducts = []
    cat = cat.lower()
    for product in mock_data:
        if product["category"].lower() == cat:
            listProducts.append(product);
    return json.dumps(listProducts)

# - GET /api/categories returns the list of unique categories on your catalog
#using sets
@app.get('/api/categories')
def categories():
    cat = set()
    for product in mock_data:
        cat.add(product["category"])
    return json.dumps(list(cat))

#using list
# def get_categories():
#     categories=[]
#     for product in mock_data:
#         if product["category"] not in categories:
#             categories.append(product["category"])  
#     return json.dumps(categories)




app.run(debug=True)


# Shows a welcome message on / (root) endpoint   ok
# - GET /api/catalog endpoint that returns a list of objects  ok
# - GET /api/catalog/api/<id> endpoint that return the product for the provided id  ok
# - GET /api/catalog/cheapest endpoint that returns the cheapest product from the catalog ok
# - GET /api/catalog/<category> returns the products that belongs to a specified category
# - GET /api/categories returns the list of unique categories on your catalog
