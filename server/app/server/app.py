from pymongo import MongoClient
from flask import Flask

MONGODB_HOST = '172.22.0.2'
MONGODB_PORT = 27017
DB_NAME = 'Your DB name'
COLLECTION_NAME = 'collectionname'

app = Flask(__name__)
  
@app.route('/')
def hello():
	client = MongoClient('172.22.0.2', 27017)
	db=client.admin
	serverStatusResult=db.command("serverStatus")
	print(serverStatusResult)
	return serverStatusResult

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8080, debug = True) 




    #serverStatusResult
  
