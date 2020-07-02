from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/")
def index():
    return "<a href='/posts'> Posts </a>"

@app.route("/response")
def response():
    headers(
        "Content-Type": "text,html"
    )
    return Response("Uma resposta do servidor", 200, headers=headers)

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
    app.run()