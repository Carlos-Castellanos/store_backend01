from flask import Flask, request
from unittest import mock
from webbrowser import get
from about import me
from data import mock_data
import json
import random
from config import db
from bson import ObjectId
from flask_cors import CORS

app = Flask('server')
CORS(app)

@app.get('/')
def home():
    return "Hello flask server: Organika <FSDI 110 class 1>"


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
def fix_mongo_id(obj):
    # fix the _id attribute
    obj["id"] = str(obj["_id"])
    # remove _id attribute
    del obj["_id"]
    return obj

@app.get('/api/products')
def get_catalog():
    cursor = db.catalog.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)
    return json.dumps(results)


#july 19 post

# Request cycled, server was restarted and working
@app.post("/api/products")
def save_product():
    try:
        newProduct = request.get_json()
        print(newProduct)
        # mock_data.append(newProduct)
        # newProduct["id"] = random.randint(1, 999999)

        # save the product
        db.catalog.insert_one(newProduct)
        fix_mongo_id(newProduct)
        print(newProduct)
        return json.dumps(newProduct)
    except ValueError as error:
        print("invalid json: %s" % error)
        return False


# Request cycled, server was restarted and working

@app.get('/api/coupons')
def get_coupons():
    # collection´s names coupons
    cursor = db.coupons.find({})
    results = []
    for coupon in cursor:
        fix_mongo_id(coupon)
        results.append(coupon)
    return json.dumps(results)

@app.post("/api/coupons")
def save_coupon():
    try:
        newCoupon = request.get_json()
        print(newCoupon)

        # save the coupon
        db.coupons.insert_one(newCoupon)
        fix_mongo_id(newCoupon)
        print(newCoupon)
        return json.dumps(newCoupon)
    except ValueError as error:
        print("invalid json: %s" % error)
        return False


# - GET /api/products/<id> endpoint that returns the products with such id


# @app.get("/api/products/<id>")
# def get_products(id):
#     cursor = db.catalog.find({})
#     for product in cursor:
#         fix_mongo_id(product)
#         if product["id"] == id:
#             print(product["id"])
#             return json.dumps(product)
#     return "Not found: " + id

@app.get("/api/products/<id>")
def get_products(id):
    product = db.catalog.find_one({"_id": ObjectId(id)})
    if product:
       fix_mongo_id(product)
       print(product["id"])
       return json.dumps(product)
    return "Not found: " + id

# - GET /api/catalog/cheapest returns the cheapest product on the list
@app.get('/api/product_cheapest')
def get_cheapest():
    cursor = db.catalog.find({})
    solution  = cursor[0]
    for product in cursor:
        if product["price"] < solution["price"]:
            solution = product
            
    fix_mongo_id(solution)
    return json.dumps(solution)


# - GET /api/catalog/expensive returns the most expensive product on the list
@app.get('/api/products_expensive')
def expensiveProduct():
    cursor = db.catalog.find({})
    maxPrice =cursor[0]
    for product in cursor:
        if product["price"] > maxPrice["price"]:
            maxPrice = product
    fix_mongo_id(maxPrice)
    return json.dumps(maxPrice)

# - GET /api/catalog/total returns the total of adding up the products' prices


@app.get('/api/products/total')
def sum():
    sum = 0
    cursor = db.catalog.find({})

    for product in cursor:
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
    cursor = db.catalog.find({"category": cat})
    listProducts = []
    for product in cursor:
        fix_mongo_id(product)
        listProducts.append(product);
    return json.dumps(listProducts)

# - GET /api/categories returns the list of unique categories on your catalog
#using sets
@app.get('/api/categories')
def categories():
    cursor = db.catalog.find({})
    cat = set()
    for product in cursor:
        cat.add(product["category"])
    return json.dumps(list(cat))

#using list
# def get_categories():
#     categories=[]
#     for product in mock_data:
#         if product["category"] not in categories:
#             categories.append(product["category"])  
#     return json.dumps(categories)


#19-jul class 1  110
# get retrun the number of prod in the catalog
# /api/count_products 

@app.get('/api/count_products')
def get_count_products():
    cursor = db.catalog.find({})
    count = 0;
    for prod in cursor:
        count += 1
    return json.dumps({"count":count})


#get /api/search/<text
#return all prod whose title contains text
@app.get('/api/search/<text>')
def search_products(text):
    cursor = db.catalog.find({})
    listProducts = []
    text = text.lower()
    for product in cursor:
        if text in product["title"].lower():
            fix_mongo_id(product)
            listProducts.append(product);
    return json.dumps(listProducts)

# /////////////////////////////////
#### api endpoint coupon codes#####




app.run(debug=True)


# Shows a welcome message on / (root) endpoint   ok
# - GET /api/catalog endpoint that returns a list of objects  ok
# - GET /api/catalog/api/<id> endpoint that return the product for the provided id  ok
# - GET /api/catalog/cheapest endpoint that returns the cheapest product from the catalog ok
# - GET /api/catalog/<category> returns the products that belongs to a specified category
# - GET /api/categories returns the list of unique categories on your catalog
