from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "this is a secret key, trust"

@app.route('/')
def index():
    if not 'number_of_checks' in session:
        session['number_of_checks'] = 0
    else:
        session['number_of_checks'] += 1
    return render_template('index.html')

@app.route('/add_visit', methods = ['POST'])
def add_visit():
    session['number_of_checks'] += 1
    return redirect('/')

@app.route('/delete_visits', methods = ['POST'])
def delete_visits():
    session['number_of_checks'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

