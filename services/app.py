#!/usr/bin/python3
from flask import Flask, jsonify, request, json
import posts_service.api

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"

@app.route('/api/posts', methods=['GET'])
def get_tasks():
    return jsonify({'POSTS': posts_service.api.get_posts()})

@app.route('/api/posts', methods=['POST', 'PUT', 'DELETE'])
def post():
    if request.method == 'POST':
        posts_service.api.add_post(request.json)
        return jsonify("Posted")


if __name__ == "__main__":
    app.run(debug=True)