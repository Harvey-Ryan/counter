

from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key='super_secret_key'

@app.route('/') #Basic route
def index():
    if 'count' not in session: #if no session
        session['count'] = 0 #set count to 0
    else:
        session['count'] += 1 #if in session
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear() #clears session returning the count to specified value on line 11
    return redirect('/') #returns home

@app.route('/2')
def two():
    session['count'] += 2 #plus 2
    return render_template('index.html')

@app.route('/3')
def three():
    session['count'] += 3 #plus 3
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)