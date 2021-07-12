from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt
import json
import random
import time
import threading
import datetime
#########################################################
#Const
RESULT = []
MAX_QUESTION = 6
COUNT = 0
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
db = client.get_database('total_records')
#get the particular collection that contains the data
records = db.register
#########################################################
def get_user_from_bd():
    users_spis = []
    
    users = records.find({})

    return users
def timedelta(): 
    start = datetime.datetime.today()
    print("Hi, you are customer ",num) 
    then = datetime.datetime.now()
    #k = datetime.datetime.today()
    delta = datetime.datetime.now() - then
    while delta.seconds != 20:
        now = datetime.datetime.now()
        delta = now - then

def ger_test():
    global RESULT
    global MAX_QUESTION
    global RANDOMQUSTION
    global COUNT
    test2 = RANDOMQUSTION
    result = []
    if COUNT >= MAX_QUESTION:
        COUNT = 0
        
        return COUNT
    if request.method == "POST":
        user_answer = request.form.get("answer")
        try:
            RESULT.append(test2[COUNT][int(user_answer)][1])
        except TypeError:
            RESULT.append(0)
    else: 
        user_answer = 0

    random_number = set()
    while len(random_number) !=4:
        random_number.add(random.randint(1,4))
    random_number = random.sample(random_number, len(random_number))
    try: 
        result.append(test2[COUNT][0])

    except IndexError:
        result.append('s')
    try:
        result.append(test2[COUNT][int(random_number[0])][0])
    except IndexError:
        result.append('s')
    try:
        result.append(test2[COUNT][int(random_number[1])][0])
    except IndexError:
        result.append('s')
    try:
        result.append(test2[COUNT][int(random_number[2])][0])
    except IndexError:
        result.append('s')
    try:
        result.append(test2[COUNT][int(random_number[3])][0])
    except IndexError:
        result.append('s')
    result.append(user_answer)
    COUNT += 1
    return result 

    

def get_qustion_from_db(level):
    global MAX_QUESTION
    list_qustion = []
    db = client.mfspbd
    qus_collection = db.question
    cursor = qus_collection.find({})
    qustion_number = set()
    while len(qustion_number) !=MAX_QUESTION:
        qustion_number.add(random.randint(1,len(cursor[0][str(level)])))

    for i in qustion_number:
     
        list_qustion.append(cursor[0][level]['question' + str(i)])

  
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
    db = client.mfspbd
    #qus_collection = db.question

    if "email" in session:
        
        if request.method == "POST":
            level = request.form.get("level")
            get_new_qustion = request.form.get("answer")
            get_new_bad_answer0 = request.form.get("bad_answer0")
            get_new_bad_answer1 = request.form.get("bad_answer1")
            get_new_bad_answer2 = request.form.get("bad_answer2")
            get_new_good_answer = request.form.get("good_answer")
            if get_new_bad_answer0 == '' or get_new_bad_answer0 == '' or get_new_bad_answer1 == '' or get_new_bad_answer2 == '' or get_new_good_answer == '':
                status = 'Данные введены не полностью'
            else:
                #db.question.insertOne()
                qus_collection = db.question
                cursor = qus_collection.find({})
                #id_collection = cursor[0]['_id']
                id_collection = 'easy_question'
                
                
                status = 'Данные отправлены'
             
                
                try:
                    k = cursor[0]
                    k[level]["question" + str(1 + len(cursor[0][level]))] = [get_new_qustion, [get_new_bad_answer0, 0.0], [get_new_bad_answer1, 0.0], [get_new_bad_answer2, 0.0], [get_new_good_answer, 1.0]]
                    db.question.remove()
                    db.question.insert_one(k)
                    return render_template('admin.html', status=status)
                except KeyError:
                    #level = 'easy_question'
                    #status = 'Данные введены не полностью'
                    return render_template('admin.html', status=status)
        return render_template('admin.html')
    else:
        return redirect(url_for("login"))
@app.route("/admin_user", methods=["POST", "GET"])
def admin_user():
    users = get_user_from_bd()
    if request.method == "POST":
        try:
            user = request.form.get("user")
            records.remove({"name":str(user)})
            status = 'dsikj'
            return render_template('admin_user.html', users=users, user=user)
        except KeyError:
            status = 'не вышло'
    return render_template('admin_user.html', users=users, user=user)

@app.route("/hardlvl", methods=["POST", "GET"])
def lvl_page():
    global RANDOMQUSTION
    marker = 'easy_question'
    try:
        marker = request.form.get("marker")
        RANDOMQUSTION = get_qustion_from_db(marker)
    except KeyError:
        marker = 'easy_question'
        RANDOMQUSTION = get_qustion_from_db(marker)
        status = 'Данные введены не полностью'
    

    return render_template('hardlvl.html')


@app.route("/test", methods=["POST", "GET"])
def test_page():
    my_result = ger_test()
    if COUNT == 0:
        return redirect(url_for('post_result'))
    else:
        return render_template('test.html', question=my_result[0], answer0=my_result[1], answer1=my_result[2], answer2=my_result[3], answer3=RESULT)
        


@app.route("/test1", methods=["POST", "GET"])
def test_page1():
    my_result = ger_test()    
    if COUNT == 0:
        return redirect(url_for('post_result'))
    else:
        return render_template('test.html', question=my_result[0], answer0=my_result[1], answer1=my_result[2], answer2=my_result[3], answer3=RESULT)
@app.route("/result")
def post_result():
    right_answer = 0
    bad_answer = 0

    for i in RESULT:
        if i == 0 or i =='None':
            bad_answer += 1
        else:
            right_answer += 1
    
    procent = (100 * int(right_answer))/MAX_QUESTION
    RESULT.clear()

    return render_template('result.html', allanswer=MAX_QUESTION , right_answer=right_answer , badanswer=bad_answer, procent=procent)


            


if __name__ == "__main__":
  app.run(host ='0.0.0.0', port = 5000,debug=True)
  #while len(random_number) !=4:
  #      random_number.add(random.randint(1,4))
  #  random_number = random.sample(random_number, len(random_number))