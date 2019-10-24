# Revamp a bonvoy dup!
# Class with inharientence, flask, and PostgressSql
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('Hey, we have Flask in a Docker container!')


@app.route("/api/v1/consumer", methods=['GET'])
def consumer():
    if request.method == 'POST':
        return add_consumer()
    if request.method == "GET":
        return get_consumer()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
