from flask import Flask, render_template
app = Flask(__name__)


@app.route('/intro')
def intro():
    return render_template("index.html")


@app.route('/rabbit')
def seeARabbit():
    return render_template("index1of2.html")


@app.route('/snail')
def seeASnail():
    return render_template("index2of2.html")

@app.route('/shiba')
def seeAShiba():
    return render_template("indexShiba.html")

# -----------------------------------


# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return "Sorry! No response. Try again"

if __name__ == "__main__":
    app.run(debug=True)
