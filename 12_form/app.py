#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#demo -- My First Flask App
#2019-09-17t

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():	
    return render_template('form.html') #generates html page with form

@app.route("/auth") #assign following fxn to run when root route requested
def authenticate():
    print(app) #prints stringified version of flask app
    print(request) #prints form request
    print(request.args) #prints form input as immutable dict
    print(request.headers) #prints form headers
    return render_template('auth.html', user = request.args["username"], method = request.method)	#generates html page using form submissions

if __name__ == "__main__":
    app.debug = True
    app.run()
