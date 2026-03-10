from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Url building in Flask"

@app.route('/Welcome/<name>')
def welcome(name):
    return "Welcome %s" % name

@app.route("/rollno/<int:num>")
def rollno(num):
    return "Your roll number is %d" % num

if __name__ == '__main__':
    app.run(debug=True, port=5100)