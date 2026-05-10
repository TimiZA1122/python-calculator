from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from maths import *
import math

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=addition(a, b))


@app.route("/subtract")
def subtract():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=subtraction(a, b))


@app.route("/multiply")
def multiply():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=multiplication(a, b))


@app.route("/divide")
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    if b == 0:
        return jsonify(result=None, error="Cannot divide by zero")

    return jsonify(result=division(a, b))


@app.route("/square-root")
def sqrt():
    a = float(request.args.get("a"))
    return jsonify(result=square_root(a))


# -------------------------
# CALCULATOR ENGINE
# -------------------------

@app.route("/calc")
def calc():
    expression = request.args.get("expression", "")

    try:
        expression = expression.strip()

        if not expression:
            return jsonify(error="Empty expression", result=None)

        result = eval(expression)
        return jsonify(result=result)

    except:
        return jsonify(error="Invalid expression", result=None)

if __name__ == "__main__":
    app.run(debug=True)