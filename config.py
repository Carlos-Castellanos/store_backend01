# con_str = "mongodb+srv://uAdmin:organika2022@organika.sanbqgc.mongodb.net/?retryWrites=true&w=majority"

# client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

# db = client.get_database("organikaDB")


import pymongo
import dns.resolver
import certifi

con_str = "mongodb+srv://uAdmin:organika2022@organika.sanbqgc.mongodb.net/?retryWrites=true&w=majority"

MONGO_DB = 'organikaDB'
MONGO_COLLECTION = 'catalog'

print("Connecting to MongoDB...")
try:
    #client = pymongo.MongoClient("mongodb+srv://uAdmin:organika2022@organika.sanbqgc.mongodb.net/?retryWrites=true&w=majority")
    client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
    #cliente.server_info()
    #print("Coneccion a mongo exitosa")    
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    #client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)
