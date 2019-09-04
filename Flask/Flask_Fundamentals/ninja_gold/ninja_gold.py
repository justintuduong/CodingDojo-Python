from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "dont forget me!"

@app.route('/') #session data goes here
def default():
    if "gold" not in session:
        session['gold'] = int(0)
    else:
        session['gold'] = session['gold']

    if 'message' not in session:
        session['message'] = ''

    if 'farm' not in session:
        session['farm']=random.randint(10,20)
        print(f"farm gold = {session['farm']}")
    else: print(f"farm gold = {session['farm']}")

    if "cave" not in session:
        session['cave'] = random.randint(5,10)
        print(f"cave gold = {session['cave']}")
    else: print(f"cave gold = {session['cave']}")

    if 'house' not in session:
        session['house'] = random.randint(2,5)
        print(f"house gold = {session['house']}")
    else: print(f"house gold = {session['house']}")     

    if 'casino' not in session:
        session['casino'] = random.randint(-50,50)
        print(f"casino gold = {session['casino']}")
    else: print(f"casino gold = {session['casino']}")

    return render_template("index.html", gold=session['gold'], message=session['message'], farm=session['farm'], cave=session['cave'], house=session['house'], casino=session['casino'])

@app.route('/process_money', methods=['POST'])
def process_money():

    newArr = [request.POST.keys()]
    print(newArr)

    session['gold'] += int(request.form['farm'])
    print(f" GORDON {session['gold']}")

    # session['gold'] += int(request.form['cave'])
    # print(f" GORDON {session['gold']}")

    # session['gold'] += int(request.form['house'])
    # print(f" GORDON {session['gold']}")

    # session['gold'] += int(request.form['casino'])
    # print(f" GORDON {session['gold']}")

    session.pop("farm")
    session.pop("cave")
    session.pop("house")
    session.pop("casino")
    # session.clear()
    return redirect('/')
    



# ------------------------------
if __name__=="__main__":
    app.run(debug=True)

