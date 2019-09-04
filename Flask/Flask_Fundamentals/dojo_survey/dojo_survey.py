from flask import Flask, render_template, request, redirect
app = Flask (__name__)

@app.route('/')
def default():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def result():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("show.html", name_from_template = name_from_form, location_from_template = location_from_form, language_from_template = language_from_form, comment_from_template= comment_from_form )
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)