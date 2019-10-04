#Ethan Chen and William Cao
#SoftDev1 pd2
#15_login flask app
#2019-10-03t

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
app = Flask(__name__)

#returns an array of which username and password is incorrect
def check_creds(username, password):
    error = []
    if (password != 'pass'):
        error.append('pass')
    if (username != 'user'):
        error.append('user')
    return error

@app.route("/")
def home():
    #if there is no session for username then go to the login page
    if (session.get('username') == None):
        return redirect(url_for("login"))
    #if there already is a session, then check if they logged in correctly.
    #if they did then welcome them, if they didnt then redirect them to the bad login page
    else:
        cred_errors = check_creds(session.get('username'),session.get('password'))
        if (len(cred_errors) == 0):
            return redirect(url_for("welcome"))
        else:
            return redirect(url_for("bad_login"))

@app.route('/login', methods = ['GET'])
def login():
    #if they didnt login already, then bring them to the login page
    if (len(request.args) == 0):
        return render_template("login.html")
    #after they press the login button then check to see if they logged in correctly
    #if they did then bring them to the welcome page and if they didnt then bring them to a bad login page
    else:
        session['username'] = request.args['username']
        session['password'] = request.args['password']
        cred_errors = check_creds(session.get('username'),session.get('password'))
        if (len(cred_errors) == 0):
            return redirect(url_for("welcome"))
        else:
            return redirect(url_for("bad_login"))

#welcomes them, if they press the logout button (we know when the post method gets activated)
#then redirect them to the logout page
@app.route("/welcome", methods = ['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        return redirect(url_for("logout"))
    return render_template('welcome.html')

#removes the sessions, brings them back to login
@app.route("/logout")
def logout():
    session.pop('username')
    session.pop('password')
    return redirect(url_for("login"))

#uses the check_creds methods to see what the errors were and prints accordingly,
#when they press the try again button (indicated by the post method) then redirect them to the login page
@app.route('/bad_login', methods = ['GET', 'POST'])
def bad_login():
    if request.method == 'POST':
        return redirect(url_for("login"))
    return render_template('bad_login.html', errors = check_creds(session.get('username'),session.get('password')))

#need secret key in order to get the code to work
if (__name__ == "__main__"):
    app.secret_key = 'super secret key'
    app.debug = True
    app.run()
