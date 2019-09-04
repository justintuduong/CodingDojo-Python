from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def default():
    if 'views' in session:
        session['views'] = session.get('views') + 1
        print(session['views'])
    else:
        session['views'] =1
        print(session['views'])
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return render_template("index.html", count = session['count'])

@app.route('/addtwo')
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


# ----------------------
if __name__=="__main__":
    app.run(debug=True)
