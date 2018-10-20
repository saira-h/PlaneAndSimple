from flask import jsonify, request, abort, Response
from flight import app
from datetime import datetime
import json
import requests

url = "http://partners.api.skyscanner.net/apiservices/"

@app.route('/', methods=['GET'])
def index(path):
    return app.send_from_directory('static', path)

@app.route('/flight/<country>/<currency>/<locale>/<originPlace>/<destinationPlace>/<inboundDate>', methods=['GET'])
@app.route('/flight/<country>/<currency>/<locale>/<originPlace>/<destinationPlace>/<outboundDate>/<inboundDate>', methods=['GET'])
def flight(country, currency, locale, originPlace, destinationPlace, inboundDate, outboundDate = None):
    if request.args:
    	api = request.args.get('api')
    	adults = request.args.get('adults')
    	children = request.args.get('children')
    	infants = request.args.get('infants')
    	includeCarriers = request.args.get('includeCarriers')
    	excludeCarriers = request.args.get('excludeCarriers')
    	groupPricing = request.args.get('groupPricing')


@app.route('/suggest/<country>/<currency>/<locale>', methods=['GET'])
def suggest(country, currency, locale):
    if request.args:
        query = request.args.get('query')
        api = request.args.get('api')
        if not api:
        	return jsonify({ 'error': 'Missing API Key' })
        if not query or len(query) < 2:
        	return jsonify({ 'error': 'Incorrect Query' })
        suggestions = get_suggestions(country, currency, locale, query, api)
        return jsonify({ 'suggestions': suggestions })

def get_suggestions(country, currency, locale, query, api):
	suggest = requests.get(url+"autosuggest/v1.0/"+country+"/"+currency+"/"+locale+"?query="+query+"&apiKey="+api)
	suggestJSON = json.loads(suggest.text)
	print(suggestJSON)
	return [{'PlaceId':x['PlaceId'],'PlaceName':x['PlaceName']} for x in suggestJSON['Places']]

