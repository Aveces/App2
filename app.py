from flask import Flask, render_template
from mymodule import cosine

app = Flask("demoApp")

@app.route("/")
def say_hello():
    return str("lol")

@app.route("/<name>")
def say_hello_with_name(name):
    return f"Hello {name}"

@app.route("/hello/<name>")
def say_hello_the__old_way_with_name(name):
    return render_template("index.html", name=name)
app.run(debug=True)

@app.route("/another")
def show_another
