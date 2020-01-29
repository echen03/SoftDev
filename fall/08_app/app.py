from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"

@app.route("/sky")
def hello_sky():
    print(__name__)
    return "clouds"

@app.route("/sea")
def hello_sea():
    print(__name__)
    return "water"

if __name__ == "__main__":
    app.debug = True
    app.run()
