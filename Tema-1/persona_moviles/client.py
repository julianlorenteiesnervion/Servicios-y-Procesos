from pymongo import MongoClient

db_client = MongoClient()

# Base de datos en remoto (ejemplo)
# db_client = MongoClient("mongodb+srv://username:password@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority")