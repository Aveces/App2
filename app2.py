from flask import Flask, request, render_template
import os
app = Flask ('posting')

@app.route('/')
def home_page():
    return 'hello'

@app.route('/hello')
def hello_page():
    return render_template('hello.html')

@app.route('/test')
def anything_lol():
    return 'test'

@app.route('/name', methods=["POST"])
def print_name():
    return request.form['name']

if 'PORT' in os.environ:
    #app running on Heroku
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    # app running locally (by typing: localhost:5000)
    app.run(debug=True)

app.run()
