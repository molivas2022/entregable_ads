from pymongo import MongoClient

# Variables
mongo_uri = 'mongodb://localhost:27017'
db_name = "message_db"
collection_name = "messages"

# Create a MongoDB client
client = MongoClient(mongo_uri)

# Connect to the database
db = client[db_name]

# Connect to the collection
collection = db[collection_name]

# Fetch and print all documents in the collection
for message in collection.find():
    print(message)

# Close the MongoDB connection
client.close()
