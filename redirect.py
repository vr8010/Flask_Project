from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)  # demo.py

@app.route('/')
def home():
    return "Flask mini project"

@app.route('/about')
def about():
    return redirect(url_for('home.html'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True, port=5100)