from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        reversed_input = user_input[::-1]
        return render_template("index.html", reversed_input=reversed_input)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
