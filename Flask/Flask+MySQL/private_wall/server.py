from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "you come here often?"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# DOB_REGEX = re.compile(r"^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](19|20)\\d\\d$" )   # DOB REGEX (test failed)
# did not test.
DOB_REGEX = re.compile(r'^[\d]{1,2}/[\d]{1,2}/[\d]{4}')

# -------------------------------------------------------------------
# login and registration page, contains POST form
# -------------------------------------------------------------------


@app.route('/')
def root():
    return render_template("index.html")

# -------------------------------------------------------------------
# POST form, REDIRECT to User main page, STILL NEED TO CHANGE PRINT STATEMENTS TO FLASH
# -------------------------------------------------------------------


@app.route('/user/register/process', methods=['POST'])
def register_process():
    mysql = connectToMySQL("user_and_logins")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
        "email": request.form['email']
    }
    email_duplicate = mysql.query_db(query, data)

    is_valid = True
    # first name validation print (test passed)
    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("Please enter your first name", "first_name")
    # last name validation print (test passed)
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Please enter your last name", "last_name")
    # if not DOB_REGEX.match(request.form['dob']):                                        # testing, not working yet...
    #     is_valid = False
        # print("Please enter your date of birth")
    # email validation w/ regex (test passed)
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!", "email")
    if len(email_duplicate) > 0:
        is_valid = False
        flash("Email already exists", "duplicate")                                          # pw is at least 8 chars, (test passed)
    if len(request.form['password']) < 7:
        is_valid = False
        flash("Password must be at least 8 characters", "password")                         # validates pw with confirm pw
    if not request.form['password'] == request.form['password_confirm']:
        is_valid = False
        flash("Password did not match", "pw_validation")
    if not is_valid:
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(
            request.form['password'])                                                       # bcrypt prints (test passed)
        mysql = connectToMySQL("user_and_logins")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(),NOW());"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
        }
        id = mysql.query_db(query, data)
        session['id'] = str(id)
        # print(id)  # Test works! 6/12/19
        # print(session['id'])
        return redirect('/user/main/'+str(id))

# -------------------------------------------------------------------
# Post form, Login
# -------------------------------------------------------------------

@app.route('/user/login/process', methods=["POST"])
def user_login_process():
    is_valid = True
    mysql = connectToMySQL("user_and_logins")                                               # query to validate email and pw in db
    query = "SELECT password, id FROM users WHERE email = %(email)s;"
    data = {
        "email": request.form['email']
    }
    result = mysql.query_db(query,data)                                                     # prints result = [{'password': pw; 'id': num}]
    session['id'] = str(result[0]['id'])
    id = session['id']
    if not bcrypt.check_password_hash(result[0]['password'], request.form['password']):
        is_valid = False
        flash("Incorrect login information. please try again!", "bad_login")
        # print (session['id'])                                                             #tests session id
    if not is_valid:
        return redirect('/')
    return redirect('/user/main/'+id)

# -------------------------------------------------------------------
# User Main Page
# -------------------------------------------------------------------

@app.route('/user/main/<id>') 
def user_main(id):
    id = session['id']
    if not id in session:
        print("not in session")
    return render_template('user_main.html')

# -------------------------------------------------------------------
# Logout page
# -------------------------------------------------------------------

@app.route('/user/logout')
def logout():
    id = session['id']                                                                      #checks whether a session id is active
    if not id in session:
        session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

