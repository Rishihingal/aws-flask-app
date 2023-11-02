from flask import Flask, render_template

app = Flask(__name__)

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return render_template("index.html", name=name)

if __name__ == '__main__':
    app.run(debug=False,port=3121, host="0.0.0.0")
