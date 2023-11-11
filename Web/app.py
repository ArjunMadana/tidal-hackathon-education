from flask import Flask, request, render_template, redirect, url_for
from run import run

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/index.html')
def index2():
    return render_template('index.html') 

@app.route('/findings.html')
def findings():
    return render_template('findings.html') 

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/StyleSheet.css")
def stylesheet():
    return render_template("StyleSheet.css")

@app.route('/process_results', methods=['POST'])
def process_results():
    name = request.form['Name']
    id = request.form['StudentID']
    gpa = float(request.form['GPA'])
    age = request.form['Age']
    marital = request.form['Marital']
    attendance = request.form['Attendence']
    prev_qual = request.form['StudentQualifications']
    displaced = request.form['Displaced']
    special_needs = request.form['SpecialNeeds']
    debtor = request.form['Debtor']
    tuition = request.form['Tuition']
    gender = request.form['Gender']
    scholar = request.form['ScholarshipHolder']
    intl = request.form['International']

    value = run(marital, attendance, prev_qual, displaced, special_needs, debtor, tuition, gender, scholar, intl, age, gpa)
    print("TEST")
    return redirect(url_for('results', value=value, name=name))

@app.route('/results/<name>/<value>')
def results(value,name):
    return render_template('results.html', name=name, value=value)


if __name__=='__main__':
    app.run(debug=True)