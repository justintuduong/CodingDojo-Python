from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

# -------------------------------------------


@app.route("/")  # show all users page
def root():
    mysql = connectToMySQL('users')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("index.html", users=users)

# # -------------------------------------------


@app.route("/add/form")  # New user form
def add_user_form():
    return render_template("add_user.html")


@app.route('/user/add', methods=['POST'])  # submission for new user
def add_user():
    mysql = connectToMySQL('users')
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    id = mysql.query_db(query, data)
    return redirect('/')


# routes to user information page / for show and edits
# Renders show page for One user
@app.route('/user/show/<id>')
def show_user(id):
    mysql = connectToMySQL('users')
    query = "SELECT * FROM users WHERE id=" + id + ';'
    users = mysql.query_db(query)
    return render_template("user_show.html", users=users, id = id)

# GET route to render html page with edit form
@app.route('/user/edit/<id>')
def update_user(id):
    mysql = connectToMySQL('users')
    query = "SELECT * FROM users WHERE id=" + id + ';'
    users = mysql.query_db(query)
    return render_template('user_edit.html', users=users)

# POST route to handle post request for edit form
# Redirect to show one user page
@app.route('/user/editing', methods=["POST"])
def submit_edit():
    mysql = connectToMySQL('users')
    query = "UPDATE users SET first_name= %(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=" + request.form['hidden']

    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email": request.form['email']
    }
    users = mysql.query_db(query,data)
    return redirect('/user/show/' + request.form['hidden'])

@app.route('/user/delete/<id>')
def delete_user(id):
    mysql = connectToMySQL('users')
    query = "DELETE FROM users WHERE id=" + id
    users = mysql.query_db(query)
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)




