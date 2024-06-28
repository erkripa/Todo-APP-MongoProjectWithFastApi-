from pymongo import MongoClient
import urllib.parse
from pymongo.server_api import ServerApi


username = "ayushonaofficial"
password = "test123"

encoded_username = urllib.parse.quote(username)
encoded_password = urllib.parse.quote(password)
 
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.zow3jnz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection_name = db['todos']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print('Error coming while onnecting')
    print(e)