from flask import Flask, render_template, request, jsonify
from utils.tools import parse
app = Flask(__name__)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("main.html")


@app.route("/result", methods=['GET', 'POST'])
def main():
    req = request.form
    first, last, age = req.get("first_name"), req.get("last_name"), req.get("age")
    req = {"full_name": parse(first, last, age), "age": age}
    return render_template("result.html", result=req)


if __name__ == "__main__":
    app.run(debug=True)
