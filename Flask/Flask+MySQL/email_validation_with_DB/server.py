from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key= "jello"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# ------------------------------------------------------
# root page, contains POST form
# ------------------------------------------------------

@app.route('/')
def root():
    print("im working")
    return render_template("index.html")

# ------------------------------------------------------
# POST redirect 
# ------------------------------------------------------

@app.route('/process', methods=['POST'])
def process():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!","email")
        return redirect("/")
    else:
        print("im working2")
        mysql = connectToMySQL("email_validation")
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(),NOW());"
        data = {
            "email": request.form['email']
        }
        mysql.query_db(query,data)
    return redirect('/success')


# ------------------------------------------------------
# Render template for successful submission
# ------------------------------------------------------

@app.route('/success')
def success():
    flash("SUCCESSSSSSSSSS!!!")
    mysql = connectToMySQL("email_validation")
    query = "SELECT * FROM emails"
    email = mysql.query_db(query)
    print(email)
    return render_template('success.html', email=email)


if __name__ == "__main__":
    app.run(debug=True)
