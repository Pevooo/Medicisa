import os
from flask import Flask, request, jsonify
from appdata import User, Question, File


app = Flask(__name__)


JSON_FAIL = {"status": "FAILED"}
JSON_SUCCESS = {"status": "SUCCESS"}

SECRET_KEY = os.getenv('MEDICISA_SECRET_KEY')


@app.route('/add/<id>', methods=["GET", "POST", "PUT"])
def update_user(id):
    user = User.get(id)
    data = request.get_json()
    if data["key"] != SECRET_KEY:
        return jsonify(JSON_FAIL)

    if request.method == "POST":
        if user is not None: return jsonify(JSON_FAIL)
        new_user = User(**data)
        new_user.add()
        return jsonify(JSON_SUCCESS)
    elif request.method == "PUT":
        if user is None: return jsonify(JSON_FAIL)
        user.update(**data)
        return jsonify(JSON_SUCCESS)

    return jsonify(JSON_FAIL)

@app.route('/get/<id>', methods=["GET", "POST"])
def get_user(id):
    user = User.get(id)
    data = request.get_json()
    if data["key"] != SECRET_KEY:
        return jsonify(JSON_FAIL)


    if request.method == "POST":
        if user is None: return jsonify(JSON_FAIL)
        if user.auth(data["password"]): return jsonify(user.details)
        else: return jsonify(JSON_FAIL)

    return jsonify(JSON_FAIL)


@app.route('/data/<question>')
def increment(question):
    data = request.get_json()
    if data["key"] != SECRET_KEY:
        return jsonify(JSON_FAIL)
    
    if request.method == "POST":
        q = Question(question)
        q.increment()
        return jsonify(JSON_SUCCESS)

    return JSON_FAIL


@app.route('/upload_report/<id>')
def upload_report(id):
    data = request.get_json()
    if data["key"] != SECRET_KEY:
        return jsonify(JSON_FAIL)
    user = User.get(id)

    user.add_file(File(data["filedata"], data["filename"]))
    return jsonify(JSON_SUCCESS)



if __name__ == "__main__":
    app.run(port=12150)
