from flask import jsonify, request, abort, Response
from flight import appw
from datetime import datetime
import json

@app.route('/', methods=['GET'])
def index():
    return jsonify({ 'hello': 'world' })

@app.route('/flight', methods=['GET'])
def flights():
    return jsonify({ 'hello': 'world' })

