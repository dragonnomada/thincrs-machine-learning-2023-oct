# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/report/1")
def report1():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    return {
        "x": x,
        "y": y
    }

app.run(port=5000, host="127.0.0.1")