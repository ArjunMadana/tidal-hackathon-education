from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prediction='HOME')

@app.route('/results')
def results():
    return render_template('results.html', prediction='YESSSSS')