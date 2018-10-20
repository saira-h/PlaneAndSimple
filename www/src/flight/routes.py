from flask import jsonify, request, abort, Response
from flight import app
from datetime import datetime
import json

@app.route('/', methods=['GET'])
def index():
    return jsonify({ 'hello': 'world' })

@app.route('/flight', methods=['GET'])
def flight():
    return jsonify({ 'hello': 'world' })

