from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checkerboard')
def checkerboardDefault():
    return render_template("index.html", row = 6, column = 6)

@app.route('/checkerboard/<x>')
def checkerboardRow(x):
    x = int(x)
    return render_template("index.html", row = x, column=6, color1 = "black", color2 = "red")


@app.route('/checkerboard/<x>/<y>')
def checkerboardRowColumn(x,y):
    x = int(x)
    y = int(y)
    return render_template("index.html", row = x, column = y)

@app.route('/checkerboard/<x>/<y>/<color1>/<color2>')
def checkboardColors(x, y, color1, color2):
    x = int(x)
    y = int(y)
    return render_template("index.html", row = x, column = y, color1 = color1, color2 = color2)

# ---------------------------------------

if __name__ =="__main__":
    app.run(debug = True)