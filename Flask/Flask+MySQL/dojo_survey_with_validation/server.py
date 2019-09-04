from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key= "dont forget about me!"

# ----------------------------------------------------------------------
# Root page
# ----------------------------------------------------------------------

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/results/<id>')
def result(id):
    mysql = connectToMySQL('dojo_surveys')
    query = "SELECT * FROM surveys WHERE id="+ id + ";"
    surveys = mysql.query_db(query)
    print(surveys)
    return render_template("results.html", surveys=surveys)

@app.route('/process', methods=['POST'])
def process ():
    is_valid = True
    if len(request.form['name']) <= 1:
        is_valid = False
        flash("Please enter a name",'name')
    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL('dojo_surveys')
        query = "INSERT INTO surveys (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        data = {
            "name": request.form['name'],
            "location": request.form['location'],
            "language": request.form['language'],
            "comment": request.form['comment']
        }
        id = mysql.query_db(query,data)
        flash("Friend successfully added!")
        return redirect('/results/'+str(id))

if __name__ == "__main__":
    app.run(debug=True)



    # mysql = connectToMySQL('dojo_surveys')
    # query = "INSERT INTO surveys (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
    # data = {
    #     "name": request.form['name'],
    #     "location": request.form['location'],
    #     "language": request.form['language'],
    #     "comment": request.form['comment']
    # }

    # id = mysql.query_db(query,data)
    # return redirect('/results/'+str(id))