from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prediction='HOME')

@app.route('/predict')
def predict():
    return render_template('index.html', prediction='YESSSSS')