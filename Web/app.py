from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/process_results', methods=['POST'])
def process_results():
    name = request.form['Name']
    id = request.form['StudentID']
    gpa = request.form['GPA']
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

    return redirect(url_for('results', name=name))

@app.route('/results/<name>')
def results(name):
    return render_template('results.html', name=name)


if __name__=='__main__':
    app.run(debug=True)