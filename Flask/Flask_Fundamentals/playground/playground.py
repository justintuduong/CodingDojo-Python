from flask import Flask, render_template
app = Flask(__name__)

# --------------------------

@app.route('/play')
def default():
    return render_template("index.html", times=3)

# --------------------------

@app.route('/play/<x>')
def multiplyBox(x):
    num = int(x)
    return render_template("index.html", times=num)

# --------------------------
@app.route('/play/<x>/<color>')
def multiplyBoxAndColor(x,color):
    num = int(x)
    return render_template("index.html", times=num, color=color)

# --------------------------
if __name__=="__main__":
    app.run(debug=True)
