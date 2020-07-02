from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return "<a href='/posts'> Posts </a>"

@app.route("/redirect")
def red():
    return redirect(url_for("/response"))

@app.route("/response")
def response():
       return render_template("response.html")

@app.route("/posts")
def posts():
    data= dict(
        path=request.path,
        referrer = request.referrer,
        content_type = request.content_type,
        method = request.method
    )
    return data

if __name__ == "__main__":
    app.run(debug=True)