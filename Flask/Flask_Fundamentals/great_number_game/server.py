from flask import Flask, render_template, request, redirect, session
import random  # import the random module
app = Flask(__name__)

# global variables
app.secret_key = "don't forget me!"

@app.route('/')
def index():
    if 'feedback' not in session:
        session['feedback']=""
    if 'color' not in session:
        session['color']=""
    if 'response' not in session:
        session["response"]=""
    if 'number' not in session:
        session['number']=random.randint(1,100)
        print(session['number'])
    else:
        print(session['number'])
    return render_template("index.html", response=session['response'], color=session['color'], feedback = session['feedback'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['number'])
    if guess == session['number']:
        session['response']= "Congrats, You've Won!"
        session['color'] = "green"
        session['feedback'] = 1
    if guess > session['number']:
        session['response']= 'Too high!'
        session['color'] = "red"
        session['feedback'] = 1
    elif guess < session['number']:
        session['response']= 'Too low!'
        session['color'] = "red"
        session['feedback'] = 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['color'] = ""
    session['number']
    session.pop("number")
    session.pop("response")
    return redirect('/')





# ------------------------
# @app.route('/')
# def default():
#     if 'rand_num' not in session:
#         session["rand_num"] = random.randint(1, 100)
#         print("I am working!")
#     else:
#         print(session['rand_num'])
#     if 'attempts' not in session:
#         session['attempts'] = 5
#     return render_template('index.html', rand_num = session['rand_num'])

# @app.route('/guess', methods=['POST'])
# def guess():
#     guess = request.form['guess']

#     if session['rand_num'] > request.form['form']:
#         feedback = "Too high!"

#     return redirect("/")

# @app.route('/reset')
# def reset():
#     session.clear()
#     print("i am working!")
#     return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)


# , guess = request.form['guess'], answer = session['answer']

    # guess_from_form = request.form['guess']

    # if int(request.form['guess']) == int(session['answer']):
    #     correct = correct

    # if int(request.form['guess']) > int(session['answer']):


        # high = "Too high!"
        # session['attempts'] -= 1

        # if int(request.form['guess']) < int(session['answer']):
        #     low = "Too low!"
        #     session['attempts'] -= 1