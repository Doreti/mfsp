from pymongo import MongoClient
from flask import Flask, request
from flask import render_template, redirect, url_for
from flask_login import LoginManager, login_required, UserMixin
from UserLogin import UserLogin
from werkzeug.security import generate_password_hash, check_password_hash

#configure
MONGODB_HOST = '172.22.0.2'
MONGODB_PORT = 27017
DB_NAME = 'mfspbd'
COLLECTION_NAME = 'users'




app = Flask(__name__)
login_manager = LoginManager()  
login_manager.login_view = 'login'
login_manager.init_app(app)

def conectBD():
	client = MongoClient(MONGODB_HOST, MONGODB_PORT)
	#db = client.DB_NAME
	db = client[DB_NAME]
	series_collection = db[COLLECTION_NAME]
	collection = series_collection.find_one()
	login = collection.get('admin')
	password = collection.get('admin').get('password')
	#return 

@login_manager.user_loader
def load_user(user_id):
	# since the user_id is just the primary key of our user table, use it in the query for the user
	return User.query.get(int(user_id))


@app.route('/')

def test():
	
	
	return render_template("test.html",title="m", question="serverStatusResult", qwestion0=conectBD(),qwestion1="asdhnoasdnasoidno", qwestion2="asdhnoasdnasoidno", qwestion3="asdhnoasdnasoidno")
	#serverStatusResult

@app.route('/login', methods=['POST', 'GET'])
def login_user():
	name = request.form.get('name')
	password = request.form.get('password')
	hashh = generate_password_hash(password)
	if check_password_hash(hashh, "admin"):
		name="yes"
		user='admin'
		login_user(user, remember=False)
	else:
		name="no"
	#os.system("echo"+str(name)+str(password)+"")
	return render_template("login.html", name=name, password=password)
@app.route('/admin')
@login_required

def admin_panel():
	return render_template("admin.html")

@app.route('/result')
def result():
	return render_template("result.html", all_qwestion="20", wrong_qwestion="4")



if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8080, debug = True) 

