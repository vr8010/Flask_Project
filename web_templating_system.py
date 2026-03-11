from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 72},
    {"name": "Amit", "marks": 91}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students")
def show_students():
    return render_template("students.html", students=students)

@app.route("/marks")
def marks():
    return render_template("marks.html", students=students)

if __name__ == "__main__":
    app.run(debug=True,port=5300)