from flask import jsonify, request, abort, Response
from flight import app
from datetime import datetime
import json
import requests

url = "http://partners.api.skyscanner.net/apiservices/"

@app.route('/', methods=['GET'])
def index():
    return jsonify({ 'hello': 'world' })

@app.route('/flight', methods=['GET'])
def flight():
    return jsonify({ 'hello': 'world' })

@app.route('/suggest/<country>/<currency>/<locale>', methods=['GET'])
def suggest(country, currency, locale):
    if request.args:
        query = request.args.get('query')
        api = request.args.get('api')
        suggestions = get_suggestions(country, currency, locale, query, api)
        return jsonify({ 'suggestions': suggestions })


def get_suggestions(country, currency, locale, query, api):
	suggest = requests.get(url+"autosuggest/v1.0/"+country+"/"+currency+"/"+locale+"?query="+query+"&apiKey="+api)
	suggestJSON = json.loads(suggest.text)
	return [x['PlaceName'] for x in suggestJSON['Places']]