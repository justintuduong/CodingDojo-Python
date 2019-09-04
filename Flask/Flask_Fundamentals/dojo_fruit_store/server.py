from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  
date_time = datetime.datetime.now()




@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout( ):
    print(request.form)
    first_name_from_form = request.form ['first_name']
    last_name_from_form = request.form ['last_name']
    student_id_from_form = request.form ['student_id']
    strawberry_from_form = request.form['strawberry']
    blackberry_from_form = request.form['blackberry']
    raspberry_from_form = request.form['raspberry']
    apple_from_form = request.form['apple']
    customer_name = request.form['first_name'] + " " + request.form['last_name']
    count = int(request.form['strawberry']) + int(request.form['blackberry']) + int(request.form['raspberry']) + int(request.form['apple'])

    return render_template("checkout.html", first_name_from_template = first_name_from_form, last_name_from_template = last_name_from_form, student_id_from_template = student_id_from_form, strawberry_from_template = strawberry_from_form, blackberry_from_template = blackberry_from_form, raspberry_from_template = raspberry_from_form, apple_from_template = apple_from_form, count = count, datetime = date_time.strftime("%b %d %Y %H:%M:%S"), customer_name = customer_name )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    