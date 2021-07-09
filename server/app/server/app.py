from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt
import json
import random
#########################################################
#Const
RANDOMQUSTION = []
DBHOST = "172.22.0.2"
DBPORT = 27017
#set app as a Flask instance 
app = Flask(__name__)
#encryption relies on secret keys so they could be run
app.secret_key = "testing"
#connoct to your Mongo DB database
client = pymongo.MongoClient(DBHOST, DBPORT)

#get the database name
#db = client.get_database('total_records')
#get the particular collection that contains the data
#records = db.register
#########################################################

def get_qustion_from_db(level):
    list_qustion = []
    db = client.mfspbd
    qus_collection = db.question
    cursor = qus_collection.find({})
    qustion_number = set()
    while len(qustion_number) !=2:
        qustion_number.add(random.randint(1,len(cursor[0][level])))

    for i in qustion_number:
     
        list_qustion.append(cursor[0][level]['question' + str(i)])

    #return cursor[0]['easy_question']

    #return level
    #return random.randint(0,100)
    #return cursor[0]['easy_question']['question2']
    #return cursor[0]['easy_question']
    return list_qustion
@app.route("/", methods=['post', 'get'])
def index():
    message = ''
    #if method post in index
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('index.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('index.html', message=message)
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insert it in the record collection
            records.insert_one(user_input)
            
            #find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('logged_in.html', email=new_email)
    return render_template('index.html')



@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")
    else:
        return render_template('index.html')

@app.route("/admin", methods=["POST", "GET"])
def admin_console():
    if "email" in session:
        return render_template('admin.html')
    else:
        return redirect(url_for("login"))

@app.route("/hardlvl", methods=["POST", "GET"])
def lvl_page():
    global RANDOMQUSTION
    marker = 'easy_question'
    #marker = request.form.get("marker")
    RANDOMQUSTION = get_qustion_from_db(marker)

    return render_template('hardlvl.html')


@app.route("/test", methods=["POST", "GET"])
def test_page():
    global RANDOMQUSTION
    test2 = RANDOMQUSTION
    spis = []

   
        #radio = request.args.get('buttonradio')
    question = 'x'
    answer0 = 'x'
    answer1 = 'x'
    answer2 = 'x'
    answer3 = 'x'
    k=0
    while k !=2:
        #radio = 'd'
        radio = request.args.get('buttonradio')
        
        if radio == 'readyanswer':
            radio = 's'
            k = k + 1
        else:
            radio = 'e'
            
            
    try: 
        question = test2[0][0]

    except IndexError:
        question = 'some qustion'
    try:
        answer0 = test2[0][1][0]
    except IndexError:
        answer0 = 'some answer'
    try:
        answer1 = test2[0][2][0]
    except IndexError:
        answer1 = 'some answer'
    try:
        answer2 = test2[0][3][0]
    except IndexError:
        answer2 = 'some answer'
    try:
        answer3 = test2[0][4][0]
    except IndexError:
        answer3 = 'some answer'
        
        #spis.append(radio)


    return render_template('test.html', question=question, answer0=answer0, answer1=answer1, answer2=answer2, answer3=answer3, spis=radio)




if __name__ == "__main__":
  app.run(host ='0.0.0.0', port = 5000,debug=True)
