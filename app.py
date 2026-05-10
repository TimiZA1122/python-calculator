from flask import Flask, request, jsonify
from flask_cors import CORS
from maths import *

app = Flask(__name__)


CORS(app)


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
    expression = request.args.get("expression")

    try:
        if not expression:
            return jsonify(result=None, error="Empty expression")

        expression = expression.replace("×", "*").replace("÷", "/")

        result = eval(expression)

        return jsonify(result=result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify(result=None, error="Invalid expression")


if __name__ == "__main__":
    app.run(debug=True)