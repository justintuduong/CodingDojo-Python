from flask import Flask
app = Flask(__name__)
@app.route('/')

#localhost:5000/ - have it say "Hello World!"
def hello_world():
    return 'Hello World!'

#localhost:5000/dojo - have it say "Dojo!"

@app.route('/dojo')
def dojo():
    return 'Dojo!'

#Create one url pattern and function that can handle the following examples:
#localhost:5000/say/flask - have it say "Hi Flask!"
#localhost:5000/say/michael - have it say "Hi Michael!"
#localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<name>')
def say_name(name):
    name = name.capitalize()
    return f"Hi {name}!"

#Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
#localhost:5000/repeat/35/hello - have it say "hello" 35 times
#localhost:5000/repeat/80/bye - have it say "bye" 80 times
#localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

@app.route('/repeat/<num>/<string>')
def repeat_num_of_str(num,string):
    return f"{string} " * int(num)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Sorry! No response. Try again"

#@app.route('/')
#def error():
#    return "Sorry! No response. Try again"

#@app.route("/")
#def function_main():
#    #all logics here
#    return render_template('index.html', pewds_sub = subsp, tseries_sub = subt)


if __name__=="__main__":
    app.run(debug=True)













