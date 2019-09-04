from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def default():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users = users)



    # <h1>Random Numbers</h1>
    # {% for number in random_numbers %}
    #     <p>{{ number }}</p>
    # {% endfor %}
    # <h1>Students</h1>
    # {% for student in students %}
    #     <p>{{ student['name'] }} - {{ student['age'] }}</p>
    # {% endfor %}







# --------------------------------
if __name__ == "__main__":
    app.run(debug=True)




# class User:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# Michael = User("Michael", "Choi")
# John = User("John", "Choi")
# Mark = User("Mark", "Guillen")
# KB = User("KB", "Tonel")